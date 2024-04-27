﻿import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import numpy as np
import time
import os
import docx2txt
import pdfplumber
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.streaming_write import write
from PIL import Image

st.set_page_config(page_title="MthoeSaps Construction Technologies", page_icon=":🗺:", layout="centered", initial_sidebar_state="expanded")


st.title("Mthoe Saps Construction Technologies Mobile App")
st.divider()

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["🏡Home","📥Services offered","🔧Project Updates & Upgrades","👨‍💼Affiliated Partners","☎Contact me here"],
    menu_icon = None,
    default_index = 0,
    )
    
if selected == "🏡Home":
    with st.container(border=False):
                   img = Image.open("mscontech_mobileapp/images and videos/Blue Orange Vintage and Retro Construction Badge Logo_20240401_174631_0000.png")
                   st.image(img, width=310, caption="Mthoe Saps Construction Technologies Trademark logo")
    st.subheader("Welcome, to the official Mthoe Saps Construction Technologies Online Platform")
    st.info("""This is my official Online Platform for my GIS, Remote Sensing and Architectural Design platform where I will be posting updates about 
            my projects that are under the Built Environment. I am supplying consultancy services as well as software engineering services for all
            problems that are related to the Built Environment Field. I am currently running a Bulawayo Mapping & Surveying beta programme for all Land Development Companies,
            Real Estate Organizations, Environmental Management Agencies, Wildlife and Recreational Parks Conservatories as well as Civil and Structual Engineers, Town 
            Planning Engineers and all interested organizations in GIS and Remote Sensing.""")
    st.info("Explore the website more to discover more about my projects and services as well as special promotionals that I will be running.")
    st.text("Click on the button below to access our Instagram page.")
    st.link_button("Mthoe Saps Construction Technologies Instagram Page", "https://www.instagram.com/mthoe_saps_construction_tech?igsh=MWZibnVpOWZkcmcyNg==")
if selected == "📥Services offered":
        st.subheader("Here are our current project abilities and services rendered out to interested parties")
        with st.container(border=False):
            st.subheader("Software development for the Built Environment Firms", divider=True)
            tab1 , tab2, tab3, tab4 = st.tabs(["Software Development","Beta Project Documentation", "3D Drone mapping and Surveying", "Architectural Drawings"])
            with tab1:
                  st.info("In this space you can get indepth knowledge on our services and ongoing projects, navigate using the tabs above.")
                  img=Image.open("mscontech_mobileapp/images and videos/Screenshot (110).png")
                  st.image(
                        img,
                        caption="Image obtained from the currently active Mthoe Saps Construction Technologies Bulawayo Mapping Survey Engine",
                        width=480,
                        channels="RGB")
                  st.subheader("Beta Project of Bulawayo Mapping and Survey Software", divider=True)
                  st.text("Click on the Preview Button to get information about this project")
                  company_status = """
                  This is a Geospatial Data web app that uses geospatial data, global positioning systems (GPS), 
                  satellites and satellite imagery as well as custom based research databases in order to properly 
                  allocate land developments. It is a very powerful tool that can be applied for a variety of purposes in 
                  The Built Environment such as policy making and zonation of towns, cities as well as communal lands (by 
                  local planning authorities) and to clearly identify hotspot areas that are prime locations for profitable 
                  land development and real estate based projects.The web app will also inhibit a Rental and Digital Marketing 
                  platform that will display all the available properties for purchase(for your asset market) or for rental 
                  purposes(for your space market). This web app will be specically dedicated to display properties as well as 
                  their about (database information) that also displays the agent who has the mandate to dispose of or lease 
                  out the property as well as the agents contact details just to promote professional practice as well as the 
                  same time mitigating unethical practices while the beta project is running. The main goal of creating this 
                  engine is to be able to create more accurate and more detailed mapping systems using geospatial data for the 
                  Built Environment in Bulawayo, Zimbabwe. With that being said, the mapping tool will be designed in accordance 
                  to the abilities of internationally compared softwares such as ArcGIS Pro, Maps Made Easy etc with more user friendlty 
                  features and easy manouvability throughout the app and an easy to navigate Graphic User Interface (GUI). You will find more 
                  information on the following tabs.
                  🌐🛰️🚁
                  """
                  def preview():
                      for word in company_status.split():
                          yield word + " "
                          time.sleep(0.05)
                  if st.button("Preview"):
                      st.write(preview)
                  st.text("Click the link below to get intouch the beta project director, Mthokozisi Thabiso Sapuwa")
                  st.write(" [WhatsApp me now to make a booking for the exciting journey ahead >](https://wa.me/263777932721)")
           
            with tab2:
                  with st.container(border=True):
                        st.subheader("Beta Project Documentation", divider=True)
                        st.write("Get a better understanding of our beta project by reading through our invitational letter and going through our complete project documentation to gain a better understanding of our project.")
                        st.write("NB: Once you apply are ready to apply for the beta project, contact the devbeloper using any of the buttons on the contact me page to receiver your sign up form bundle.")
                        st.text("Use the select box below to navigate through the documentation")
                  Documentation = ["Beta Project Invitation", "Beta Project Documentation", "Project Legal Documentation", "Beta project timeline schedule", "Research Progress Documentation", "Beta project pricing"]
                  choice = st.selectbox("Menu", Documentation)
                  if choice == "Beta Project Invitation":
                       with st.container(border=True):
                            st.subheader("Beta Project Invitation")
                            st.info("Here is our official documentation to our beta programme")
                            docx_file = "mscontech_mobileapp/Bulawayo mapping Documentation/beta project invitation letter.docx"
                            raw_text = docx2txt.process(docx_file)
                            st.text(raw_text)
                  if choice == "Beta Project Documentation":
                       with st.container(border=True):
                            st.subheader("Beta Project Documentation")
                            st.info("Here is our official project documentation")
                            docx_file = "mscontech_mobileapp/Bulawayo mapping Documentation/beta project documentation.docx"
                            raw_text = docx2txt.process(docx_file)
                            st.text(raw_text)
                  if choice == "Project Legal Documentation":
                       with st.container(border=True):
                            st.subheader("Project Legal Documentation")
                            st.info("Here is our official project legal documentation structure")
                            docx_file = "mscontech_mobileapp/Bulawayo mapping Documentation/legal documentation .docx"
                            raw_text = docx2txt.process(docx_file)
                            st.text(raw_text)
                  if choice == "Beta project timeline schedule":
                       with st.container(border=True):
                            st.subheader("Project timeline")
                            st.info("Here is our official project timeline schedule structure")
                            docx_file = "mscontech_mobileapp/Bulawayo mapping Documentation/timeline schedule.docx"
                            raw_text = docx2txt.process(docx_file)
                            st.text(raw_text)
                  if choice == "Research Progress Documentation":
                       with st.container(border=True):
                            st.subheader("Research Proress")
                            st.info("Here is our official research progress and development report")
                            docx_file = "mscontech_mobileapp/Bulawayo mapping Documentation/Research progress Documentation .docx"
                            raw_text = docx2txt.process(docx_file)
                            st.text(raw_text)
                  if choice == "Beta project pricing":
                       with st.container(border=True):
                            st.subheader("Pricing structure of the beta project")
                            st.info("Here is our official beta project pricing structure")
                            docx_file = "mscontech_mobileapp/Bulawayo mapping Documentation/pricing list.docx"
                            raw_text = docx2txt.process(docx_file)
                            st.write(raw_text)   
            with tab3:
                st.subheader("About our Drone Mapping and Surveying Programme")
                with st.container(border=True):
                        st.info("Regulalrly check on this page in order to keep up with our Drone Mapping and Surveying project. Turn on website post notifications so as to not miss any of our updates.")
                        st.info("We will use this tab in order to keep you fully updated with our exciting Drone Programming as well as our Drone Mapping and Surveying Journey. Join our beta project today so that you do not get left behind with the latest technovative news and softwares in Bulawayo. ")
                img=Image.open("mscontech_mobileapp/Bulawayo Mapping Documentation/bulawayo mapping images/5c5d6d87d2d67950c36ae48584f66880.jpg")
                st.image(
                         img,
                         #caption="Image obtained from the currently active Mthoe Saps Construction Technologies Bulawayo Mapping Survey Engine",
                         width=480,
                         channels="RGB")
            with tab4:
                 st.subheader("Prototype architectural projects run by Ambitious Designs")
                 st.subheader("Ambitious Designs Contact Card", divider=True)
                 st.info("We Provide house plans and general floor plan designs for all suitiors. Contact us now for a quotation.")
                 st.info("Use the link bellow to get intouch with us for your dream houseplan design. ")
                 st.write(" [Contact Ambitious Designs > ](https://wa.me/263715313827)")
                 img=Image.open("mscontech_mobileapp/Bulawayo Mapping Documentation/Ambitious designs work/IMG-20240405-WA0002.jpg")
                 st.image(
                      img,
                      caption="This is a subsidory firm that deals with Architectural Drawings & Designs for your concenience",
                      width=440,
                      channels="RGB")

if selected == "🔧Project Updates & Upgrades":
     st.subheader("Stay up to date with my project dashboard")
     st.info("Regularly check on this page in order to get a close preview of our upcoming projects and software updates 😉") 
      
if selected == "👨‍💼Affiliated Partners":
    st.subheader("Here is a comprehensive list of our beta project affiliated partners")
    #st.info("Use this page to view of partners organizational description and use the contact links below to get in contact with them.")
    st.info("These companies are direct affiliates to this project, this means they gets first hand information of this project")
    img=Image.open("mscontech_mobileapp/images and videos/b99da924bb802ae7db7628d507c8585c.jpg")
    st.image(
              img,
                caption="Affiliated companies caption to be posted here",
                width=200,
                channels="RGB")
    st.write(" [Contact Ambitious Designs > ](https://wa.me/263715313827)")
    img=Image.open("mscontech_mobileapp/images and videos/b99da924bb802ae7db7628d507c8585c.jpg")
    st.image(
              img,
                caption="Affiliated companies caption to be posted here",
                width=200,
                channels="RGB")
    st.write(" [Contact Ambitious Designs > ](https://wa.me/263715313827)")
    img=Image.open("mscontech_mobileapp/images and videos/b99da924bb802ae7db7628d507c8585c.jpg")
    st.image(
              img,
                caption="Affiliated companies caption to be posted here",
                width=200,
                channels="RGB")
    st.write(" [Contact Ambitious Designs > ](https://wa.me/263715313827)")
    img=Image.open("mscontech_mobileapp/images and videos/b99da924bb802ae7db7628d507c8585c.jpg")
    st.image(
              img,
                caption="Affiliated companies caption to be posted here",
                width=200,
                channels="RGB")
    st.write(" [Contact Ambitious Designs > ](https://wa.me/263715313827)")
    img=Image.open("mscontech_mobileapp/images and videos/b99da924bb802ae7db7628d507c8585c.jpg")
    st.image(
              img,
                caption="Affiliated companies caption to be posted here",
                width=200,
                channels="RGB")
    st.write(" [Contact Ambitious Designs > ](https://wa.me/263715313827)")

if selected == "☎Contact me here":
    st.info("Use the buttons below to contact the project Developer, Mthokozisi Thabiso Sapuwa in order to get your beta project signup documentation form ")
    st.subheader("Use the buttons below to get in touch with me", divider=True )
    st.link_button("Contact me on WhatsApp", "https://wa.me/263777932721") 
    st.link_button("Email me here", "https://mthoesaps06@gmail.com") 
    st.link_button("View my LinkedIn Profile", "https://www.linkedin.com/in/mthokozisi-sapuwa-1ab2151ab?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app") 
    st.link_button("Find me on Instagram", "https://www.instagram.com/mthoe.zw?utm_source=qr&igsh=MTlrZWlvdW1pNGI4bA")
    st.link_button("Check me out Facebook", "https://www.facebook.com/mthokozisi.sapuwa.50?mibextid=kFxxJD")
    
        