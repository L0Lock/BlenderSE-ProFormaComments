# BlenderSE-ProFormaComments
Tailored for [Blender Stack Exchange](https://blender.stackexchange.com/) to be used with [SE-AutoReviewComments: AutoReviewComments - Pro-forma comments for SE](https://github.com/Benjol/SE-AutoReviewComments?tab=readme-ov-file#installation)

Install the above extension/userscript. Then you can either import or [remote](https://stackapps.com/questions/2116/autoreviewcomments-pro-forma-comments-for-se/3281#3281) the raw [comments.jsonp](https://raw.githubusercontent.com/L0Lock/BlenderSE-ProFormaComments/master/comments.jsonp) file.

> [!Warning]
> It seems that getting remote is bugged out anyway:
> [Importing remote, or any JSON · Issue #132 · Benjol/SE-AutoReviewComments](https://github.com/Benjol/SE-AutoReviewComments/issues/132#issuecomment-2249041323)

## Adding new entries

Here are some templates to add new entries:

```json
  // Finish every {} with a comma, except the last one of the list!
  // Templates of Question only, Answer only, and common messages.
  { "name": "[Q]name", "description": "Message."},
  { "name": "[A]name", "description": "Message."},
  { "name": "name", "description": "Message."},
```
From [Benjol/SE-AutoReviewComments: AutoReviewComments - Pro-forma comments for SE](https://github.com/Benjol/SE-AutoReviewComments?tab=readme-ov-file):

> ***Differentiated comments for questions/answers***
> 
>    If you prefix your comment title with `[Q]`, it will be only displayed for questions, etc (see below). Non-prefixed comments are always displayed.
> 
> - Closure : "C",
> 
> - CommentQuestion : "Q",
> 
> - CommentAnswer : "A",
> 
> - EditSummaryAnswer : "EA",
> 
> - EditSummaryQuestion : "EQ"
>   
>   The expected format for the title prefix (in the import/export dialogue) is: `###[Q] More than one question asked`
