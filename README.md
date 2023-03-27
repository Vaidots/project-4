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
