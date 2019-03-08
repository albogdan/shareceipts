# Shareceipt

## What it does
Our simple web app allows for you to upload your receipt, and digitally invoice your friends for their meals. We created it at a McGill University hackathon (McHacks) in 2019. We won the prize for the "Best Newbies"

## Inspiration
We were inspired by the Interac API, because of how simple it made money requests. We all realized that one thing we struggle with sometimes is splitting the bill, as sometimes restaurants don't accommodate for larger parties.

## How we built it
For processing the receipts, we used Google Cloud's Vision API, which is a machine learning application for recognizing and converting images of characters into digital text. We used HTML, CSS, JavaScript, and JQuery to create an easy-to-use and intuitive interface that makes splitting the bill as easy as ever. Behind the scenes, we used Flask and developed Python scripts to process the data entered by the users and to facilitate their movement through our interface. We used the Interac e-Transfer API to send payment requests to the user's contacts. These requests can be fulfilled and the payments will be automatically deposited into the user's bank account.

## Challenges we ran into
The Optical Character Recognition (OCR) API does not handle receipts format very well. The item names and cost are read in different orders, do not always come out in pairs, and have no characters that separate the items. Therefore we needed to develop an algorithm that can pick up the separate the words and recognize which characters were actually useful. The INTERAC e-Transfer API example was given to us as an React app. Most of us have had no experience with React before. We needed to find a way to still be able to call the API and integrate the caller with the rest of the web app, which was build with HTML, CSS, and Javascript. There has also been a few difficulties with passing data from the front end interface and the back end service routines.

## Accomplishments that we're proud of
It's the first hackathon for two of our team members, and it was a fresh experience for us to work on a project in 24 hours. We had little to no experience with full stack development and Google Cloud Platform tools. However, we figured out our way step by step, with help from the mentors and online resources. We managed to integrate a few APIs into this project and tied together the front end and back end designs into a functional web app.

## What we learned
How to call Google Cloud APIs How to host a website on Google Cloud Platform How to set up an HTTP request in various languages How to make dynamically interactive web page How to handle front end and back end requests

## What's next for shareceipt
We hope to take shareceipt to the next level by filling in all the places in which we did not have enough time to fully explore due to the nature of a hackathon. In the future, we could add mobile support, Facebook & other social media integration to expand our user-base and allow many more users to enjoy a simple way to dine out with friends.

## Built With
### Python, Javascript, HTML, CSS
