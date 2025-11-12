// Client designed to handle API data requests
var client = {
    endpoints: {},
    token:"",
    init: function(openapi_url, token) {
        client.token = token;
    
        return axios.get(openapi_url, {
            headers: {
                'Accept': 'application/json',
                // 'Authorization': `Token ${token}`
            }
        }).then(function (response) {
            // console.log("OpenAPI Response:", response.data);  
            if (!response.data.paths) {
                throw new Error('No paths found in OpenAPI schema');
            }
            
            client.endpoints = {};  // Reset endpoints
            for(var key of Object.keys(response.data.paths)) {
                for (var method of Object.keys(response.data.paths[key])) {
                    endpoint = {};
                    endpoint['path'] = key;
                    endpoint['parameters'] = response.data.paths[key][method].parameters;
                    endpoint['operationId'] = response.data.paths[key][method].operationId;
                    endpoint['method'] = method;
                    client.endpoints[endpoint['operationId']] = endpoint;
                }
            }
            // console.log("Initialized endpoints:", client.endpoints);  // Log the endpoints
        });
    },
    get_endpoint_names: function(){
        // Get the names of the endpoints as returned by from the openapi endpoint
        return Object.keys(client.endpoints);
    },
    query: function(operationId, params) {
        // Query an endpoint for data by the operationId string of that endpoint.
        // params should be a object, with keys that correspond the parameter names.

        // Gather endpoint data
        var endpoint = client.endpoints[operationId]
        
        // Set the path
        var path = endpoint.path
        
        // Replace parameters in the path with the values passed
        for (var param of endpoint.parameters)
            path = path.replace(`{${param.name}}`, params[param.name])

        // Set up the request config, including the Token authentication/authorization and all the params in the post body and/or get query.
        const config = {
            method: endpoint.method,
            url: path,
            headers: {
                // 'Authorization': `Token ${client.token}`,
                'Accept': 'application/json' 
            },
            params: params
        }

        // Promise returned for handling.
        return axios.request(config)
    }
}

var ws_client = {
    socket: '',
    init: function() {
        log = console.log
        socket = new WebSocket('ws://'+document.location.hostname+':8001');
        socket.onmessage = this.onmessage
        socket.onopen = this.onopen
        socket.onclose = this.onclose
    },
    onopen: (event)=>{
        log("~~~~~~~~Server is connected!!!~~~~~~~~")
        socket.send("Server?")
    },
    onmessage: (event)=>{
        log("Server says: " + event.data)
    },
    onclose: (event)=>{
        log("~~~~~~~~Server disconnected!!!~~~~~~~~")
    },
}