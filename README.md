# Python_Webapp_Analysis_Analytics_Tools

## Description

### This project is to get a basic understanding of building web applications using python, hosting it in cloud using Microsoft Azure and making use of most of the azure services.This app has 2 functions 
* Analysis -  Providing visual representation of no of cars manufactured by companies in past.
* Analytics - Based on past data predicting no of cars that can be manufactured in future.

## Code Quality
![pylintss](https://user-images.githubusercontent.com/84438487/130182266-a8b30ec2-3569-4f0f-8043-927e56a3305c.png)

## Build and Deploy Badge
[![Azure App Service - Carwebapp(Production), Build and deploy Python app](https://github.com/99004324-MehulKothari/Python_Webapp_Analysis_Analytics_Tools/actions/workflows/main_carwebapp.yml/badge.svg)](https://github.com/99004324-MehulKothari/Python_Webapp_Analysis_Analytics_Tools/actions/workflows/main_carwebapp.yml)

![status](https://user-images.githubusercontent.com/84438487/130188464-a42c0ca8-644e-4ceb-b4a3-e8a86e03b3f1.jpeg)



## Folder Structure
Folder             | Description
-------------------| -----------------------------------------
`1_Requirements`   | Documents detailing requirements and research
`2_Design`         | Documents specifying design details

## Contribution Summary
PS No. |  Name   |  Contribution |Issues Raised
-------|---------|--------------|---------
`99004319` | Bharani Surya S |Database management and Azure Services |5|
`99004324` | Mehul Kothari  |Web app development and Azure Services |5|

## Challenges Faced and How was it overcome

1.	Overload of software which lead to overuse of request time- using CDN
2.	Not using pre-uri waf(web application firewall) which could lead to not giving admin access in app itself
3.	Rendering the analysis result in the same thread , solution - used pygal library.
4.	Data sharing – using bulk share and sqlcmd.

## References
* https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create
* https://azure.microsoft.com/en-in/services/app-service
* https://docs.microsoft.com/en-us/azure/cdn/cdn-add-to-web-app
* https://marczak.io/posts/azure-loading-csv-to-sql
* https://docs.microsoft.com/en-us/azure/azure-monitor/overview
* https://www.w3schools.com/tags/tag_button.asp
* https://www.w3schools.com/html/html_form_attributes_form.asp
* http://www.pygal.org/en/stable
* https://docs.sdl.com/801922/570899/sdl-tridion-docs-13-sp2/microsoft-sql-server-ports
* https://www.sqlshack.com/bcp-bulk-copy-program-command-in-action

