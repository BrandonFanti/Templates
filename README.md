 
# My templates
## --- "Start doing stuff" (faster) starter-pack 

### mamba_meta - AKA: The MAMBA_SUPER_META folder
The [<20 line sample here](https://github.com/BrandonFanti/Templates/blob/e808f016f7b99540f2b8433c21620a93f7c09f99/Python/mamba_meta_demo.py) can produce these awesome traces:

[![mamba preview](https://img.youtube.com/vi/rsQZQDLlt0s/0.jpg)](https://www.youtube.com/embed/rsQZQDLlt0s)

Currently installable via clone, and with an externally activated poetry install:

`cd $cloned_repo/Python/MAMBA_SUPER_META; poetry install`

### Package+module planning
- mamba
  - meta
    - description: 100% native python (no external dependencies)
    - util ([e.g.](https://github.com/BrandonFanti/Templates/blob/861d719f7aeb7a41a4edba269ee6c90fbc0e171b/Python/MAMBA_SUPER_META/general/filters.py#L1C5-L1C16))
    - debug
      - notably, [Protector](https://github.com/BrandonFanti/Templates/blob/5ca6ea07e50e49093cff55e4bfa68581444271c7/Python/MAMBA_SUPER_META/debug/decorators.py#L12) decorator, as demonstrated above
    - logging
    - thread
      - description despite the name, this will be general multiprocessing+threading utilities 
        - The aim is fast templates OK! Semantics...
  - interwebnet
    - an abstraction API into mamba.web+mamba.net
  - web
      - description: django driven, planning better [channel integration](https://channels.readthedocs.io/en/latest/#django-channels)
  - net
      - description: [scapy](https://scapy.readthedocs.io/en/latest/introduction.html) driven, planning better class/building heirarchy
  