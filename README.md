# FOODY Recipe Blog !!
At our food recipe blog, we're passionate about cooking and sharing our love of food with other. Our symbol, a represents our commitment to bringing you delicious recipes that are easy ti make. We started this blog because we believe that good food brings people together. We've worked hard to create a beautiful and user-friendly website that makes it easy for you to find and try out our recipes. As food lovers, we're always on the lookout for new and exciting recipes to share with our readers. We hope that our blog inspires you ti get creative in the kitchen

![responsive](/media/images/I%20am%20responsive.jpg)


## Test Cases

The following table outlines the test cases that have been performed on the application:

| Test Case Description                          | Steps                                                                                                                                          | Expected Result                                                                              | Pass/Fail |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------- |
| User can register an account                   | 1. Go to registration page <br> 2. Fill out registration form <br> 3. Click "Submit" button                                                    | User is redirected to login page with success message displayed                              | Pass      |
| User can login to their account                | 1. Go to login page <br> 2. Enter valid login credentials <br> 3. Click "Login" button                                                         | User is redirected to home page with welcome message displayed                               | Pass      |
| User can create a new post                     | 1. Go to create post page <br> 2. Fill out post form <br> 3. Click "Submit" button                                                             | Post is created and displayed on home page                                                   | Pass      |
| User can view their own post                   | 1. Go to home page <br> 2. Click on the post title                                                                                             | Post detail page is displayed with post content and comments                                 | Pass      |
| User can edit their own post                   | 1. Go to post detail page <br> 2. Click "Edit" button <br> 3. Edit post content <br> 4. Click "Submit" button                                  | Post is updated and displayed on home page                                                   | Pass      |
| User can delete their own post                 | 1. Go to post detail page <br> 2. Click "Delete" button <br> 3. Confirm deletion                                                               | Post is deleted and no longer displayed on home page                                         | Pass      |
| User can view other users' posts               | 1. Go to home page <br> 2. Click on another user's post title or "View" button                                                                 | Post detail page is displayed with post content and comments                                 | Pass      |
| User can like/unlike a post                    | 1. Go to post detail page <br> 2. Click "Like" or "Unlike" button                                                                              | Like count is updated and success message is displayed                                       | Pass      |
| User can leave a comment on a post             | 1. Go to post detail page <br> 2. Fill out comment form <br> 3. Click "Submit" button                                                          | Comment is added and displayed on post detail page with success message displayed            | Pass      |
| User cannot edit or delete someone else's post | 1. Go to recipe detail page of another user's post <br> 2. Check for edit and delete buttons <br> 3. Attempt to edit or delete the recipe post | User should not see edit or delete buttons and should not be able to edit or delete the post | Pass      |
| User can't submit a blank comment              | 1. User trie to submit an empty comment                                                                                                        | User receives an error message, for blank comment                                            | Pass      |

_All button functionality is working properly and success messages disappear after 3 seconds._

| Test Case Description                               | Steps                                                                                                                              | Expected Result                         | Pass/Fail |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | --------- |
| Error 404 page is displayed for non-existing pages  | 1. Enter a non-existing URL in the browser                                                                                         | The browser displays the error 404 page | Pass      |
| Error 500 page is displayed for server errors       | 1. Intentionally cause a server error, for example by removing a required file or misconfiguring the server                        | The browser displays the error 500 page | Pass      |
| Error 403 page is displayed for forbidden access    | 1. Attempt to access a page or resource that the user does not have permission to access, for example by entering a restricted URL | The browser displays the error 403 page | Pass      |
| Error 405 page is displayed for invalid HTTP method | 1. Attempt to use an invalid HTTP method for a resource, for example by using GET instead of POST or PUT                           | The browser displays the error 405 page | Pass      |


# User Experienc (UX)

Someone who would be interested in FOODY recipe blog app, potentiially a wide range of users who are interested in cooking and trying out new recipes such us : Home cooks , food enthusiasts, beginner cooks, health-conscious and etc.

## Project Goals:

The primary goal for this project is to create a food recipe blog, that enables full CRUD functionality : See posts of other people, after registering, are able to Create,Add, Delete their own blog posts, Comment, interact with other peoples blog posts.

## Agile Methodology

Github projects were used to manage the the development process using agile approach. 16 issues were created and implemented using Kanban board. To check the created issues you can visit [here](https://github.com/Vaidots/project-4/issues)

## User Stories

* USER STORY:View post  
As a Site user I can view a list of posts so that I can select one of them to read
* USER STORY:Open a post  
As a Site user I can click on a post so that I can see the full content
* USER STORY:Like / Unlike  
As a Site user I can like or unlike a post so that I can interact with the post
* USER STORY:View likes  
As a Site user / Admin I can view the number of likes on the posts so that I can see the popularity of the posts
* USER STORY:Comment on a post  
As a Site User I can leave a comments on a post so that I can be involved in the conversation
* USER STORY:View Comments  
As a Site User / Admin I can view comments on an individual post so that I can read the conversation
* USER STORY:Account registration  
As a Site User I can register an account so that I can comment and like
* USER STORY:Manage posts  
As a Site Admin I can create,read,update and delete posts so that I can manage my blog content
* USER STORY:Site pagination  
As a Site User I can view a paginated list of posts so that easily select a post to view
* USER STORY:Approve comments  
As a Site Admin I can approve or disapprove comments so that I can choose which comments are appropriate
* USER STORY:Create draft  
As a Site Admin I can create draft posts so that I can complete my post later
* USER STORY: Add Post  
As a site user I can add/create a post so that ** I can share my recipe with everyone**
* USER STORY: Edit a post  
As a site user I can Edit my post so that ** I can improve or fix my recipe**
* USER STORY: Delete post  
As a site user I want to be able to delete the recipe I can remove any content that I no longer want**
## Usert story not yet implemented
* USER STORY: Edit comment  
As a site user I can edit my comments so that I can correct any mistakes or typos, add additional information
* USER STORY: Delete comment  
As a user I can delete my own comments so that I can romve any content that I no longer want or think it is inappropriate or irrelevent

# Design

The blog has a very simple and minimalistic design, very very basic, white body with black, footer and navbar. I chose it due to simplicity of it and for users to be more engage with recipe posts.

# Features

## Navigation bar

Fully resposinve navigation bar, with different links, before and after login.

Before singing in

![Before-login](/media/images/be%20logina.JPG)

After, the user can Add recipes.

![Afet-signin](/media/images/navbar%20isiloginus.JPG)

## Call to action section

![Call-to-action](/media/images/call%20to%20action.JPG)

* The home page includes a supportive, motivational, call to register button which then links to a signig up form. After the user is signed uped, it changes to another motivational message with a "lets do it " button.

![After-login](/media/images/after%20login%20homepage.JPG)


## Post Section

* This section displays all recipes from all the users
* The recipe cards are paginated after 6 recipes.
* Each displays the recipes image,title,author, when posted and how many likes it has.
* Clicking on the title will open the post
![PostSection](/media/images/Post%20Section.JPG)

##  Recipe detail

* This section displays full pictures, descriptio, ingredients, instructions 
* There is also a prep and cook time displayed with likes and comment number.
![Recipe-details](/media/images/Recipedetails.JPG)

## Comment section 

* A comment box is shows with posting names user.
![Comment](/media/images/Comment%20section.JPG)

* after the comment is approved by admin the message appears on the post

![Approved-comment](/media/images/Approvedcomment2.JPG)

## Edit Post

* When user want to edit his post, he will be linked to edit post form, where user is able to edit every section he wants.

![EditPost](/media/images/Editingpost.JPG)

## Delete post

* On the other hand if the user is not happy with recipe, he can delete it. 

![DeletePost](/media/images/DeletePost.JPG)

## Add recipe

* Users can add recipe, when they press "Add recipe" link, and will need to fill the form.

![Addrecipe](/media/images/ADDrecipe.JPG)