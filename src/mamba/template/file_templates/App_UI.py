content="""<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>{}</class>
 <widget class="QMainWindow" name="{}">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>857</width>
    <height>703</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="MinimumExpanding" vsizetype="MinimumExpanding">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>{}</string>
  </property>
  <property name="styleSheet">
   <string notr="true">border-color: rgb(255, 0, 0);
border-style: solid;
border-width: thick;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="sizePolicy">
    <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
     <horstretch>0</horstretch>
     <verstretch>0</verstretch>
    </sizepolicy>
   </property>
   <property name="minimumSize">
    <size>
     <width>800</width>
     <height>600</height>
    </size>
   </property>
   <layout class="QGridLayout" name="gridLayout_3">
    <item row="0" column="0">
     <widget class="QTabWidget" name="tabWidget">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
        <horstretch>1</horstretch>
        <verstretch>1</verstretch>
       </sizepolicy>
      </property>
      <property name="tabShape">
       <enum>QTabWidget::TabShape::Rounded</enum>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="menu_widget_1">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <attribute name="title">
        <string>Main</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout">
        <item>
         <layout class="QVBoxLayout" name="menu_layout_1">
          <property name="sizeConstraint">
           <enum>QLayout::SizeConstraint::SetNoConstraint</enum>
          </property>
         </layout>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="menu_widget_2">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <attribute name="title">
        <string>Alt</string>
       </attribute>
       <layout class="QGridLayout" name="gridLayout">
        <item row="0" column="0">
         <layout class="QVBoxLayout" name="menu_layout_2"/>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>24</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuMenu1">
    <property name="title">
     <string>File</string>
    </property>
    <addaction name="actionOpen"/>
   </widget>
   <widget class="QMenu" name="menuMenu2">
    <property name="title">
     <string>Edit</string>
    </property>
   </widget>
   <addaction name="menuMenu1"/>
   <addaction name="menuMenu2"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="actionOpen">
   <property name="text">
    <string>Open</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

from os import makedirs
from os.path import sep

def export_ui(name, destination):
    dest_path = destination+sep+"app"+sep+"UI"+sep
    try:
        makedirs(dest_path)
    except:
        pass

    print()

    with open(f"{dest_path}window.ui", 'w') as fout:
        fout.write(content.format(
          name,name,name
        ))