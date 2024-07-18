# Testing - Filmlab Productions

![Home](assets/readme_img/home.png)

---
## Contents:
  * [W3C Validator](#w3c-html-validaton)
  * [Jigsaw](#jigsaw-css-validation)
  * [Testing User Stories](#testing-user-stories)
---


## Jigsaw CSS Validation
    
| Bug (class)   | Error  | Soloution & Result |
| :------------ |:---------------| :-----|
|.oneByOne|"Too many values or values are not recognized : 20px 1em"| By removing the additional "1em" nothing visible on the page changed |
|.inLine .mainTitle|"Value Error : text-align centre is not a text-align value : centre"|I fixed the typo of "center", however this still does not impact the webpage visually|
|.pcLogo |centre is not a align-items value : centre| This was tghe same issue as above, but once it was resolved, the effect was noticable, as the pc logo now sat in the middle of the nav-bar, as it was intended to|
|.navbar-nav|in is not a transition value : transform 0.4s ease in |I removed this because the code was meant to create a transition between the navbar sidepannel appearing and diappearing, however, it did not function in this way |

![Jigsaw CSS](assets/readme_img/jigsawcssvalidator1.png)

The following 'errors' did not affect my code in any meaningful way, and by removing this code, my website would loose features. For example, code such as "-webkit-tap-highlight-color: transparent;" can have a positive effect on the webpage, such as removing the blue box when a button on a mobile is clicked, improving mobile UX.

![Jigsaw CSS](assets/readme_img/jigsawcssvalidator.png)


## W3C HTML Validation

### *index.html:*

| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |


### *films.html:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |


### *about.html:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |



### *bts.html:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
| Attribute src not allowed on element button|Since src is not the correct element to apply to a button I applied the img tag instead |Pass|

### *Films section | Kidnapped |Killer Santa | Once Upon a Time:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
|"Attribute src not allowed on element button"|Since src is not the correct element to apply to a button I applied the img tag instead |Pass|
|"The frameborder attribute on the iframe element is obsolete"|Since the value of the item was 0, it was unnecesarry to include any further|Pass|
|"Error from using 'p5' as a child element for a 'ul'"|To counteract this I changed the child to "li" and targeted the new list items with the following properties "list-style: none; display: inline;" so they behave as they did before|Pass|
|"Error: No li element in scope but a li end tag seen"|Deleted surplus "li" tag|Pass|

## PEP8 - app.py

  In my code there were no major errors. Only referingto white spaces and and lines being too long. In this regard the code fails these tests. However the end user will not experience any errors due to them.

## Testing User Stories:

### First Time Visitor
| User Story |Pass or Fail |Soloution & Result |
| :---- |:-- |:-------|
|1 - To quickly find out what products Ssell is offering|Pass|Finding Ssell's newest products are easy, it is the first thing that a site visitor will see when they enter the page. When loading the homepage (which is also reached by clicking 'Seafood-Sell'), the user will be greeted with a array of products with the corrisponding image for said product.|
|2 - To find out if Ssell is a legitimate business, does this webapp legitimise the company?|Pass|On Ssell finding out if it is a legitimate supplier is simple. A user can navigate through the products listed in the home page, or contact the company via the email listed below. The only thing that I could do in the future to improve this would be to allow reviews on the website itself, providing greater authenticity.|
|3 - To find out information on the team behind Ssell, follow the latest news about the company, where the company is based, and to contact the company directly.|Pass|On this site, the user is able to stay up to date with the about us page. However, this is still lacking some features and needs to be improved to provide more information.|
|4 - What the company is about and where they source their items.|Pass|Activists and nutritunalists usually like to know where their food came from and if they meet rigorous tests and procedures before arriving to the customer. This is easily accessible underneath the description of the product, where it describes everything about the product in detail. However, the information listed is limited due to my own time constraints with writing descriptions on each item.|

### Returning Visitor GOAL
| User Story |Pass or Fail |Soloution & Result |
| :---- |:-- |:-------|
|1 - One user might be an admin or owner of the website. This user would require a way to list and describe new items, along with the ability to edit existing ones.|Pass|The Admin user can create new items, add or remove an image and change the description/ catagory of the item.|
|2 - Look for discounts or sales at that time|Fail|While prices are listed on the site, the items do not show a before and after, making it challanging for users to compare yesterdays price to the price of today. For this reason, it does not pass this test for me.|
|3 - Be able to contact the business regarding business enquiries|Pass|Investors will have an inherent interest in contacting the company directly. To navigate to this section, there is one method. To go to the navigation bar, on 'contact us' and it opens the email app. However, this may not be the best experience as it takes the user off the page. This is easily accomplished through the "Contact us" hyperlink. However, as this takes the user to another app, this can be seen as less desirable for the user.|
