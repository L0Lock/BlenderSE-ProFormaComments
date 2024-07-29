# BlenderSE-ProFormaComments

> [! Warning]
> As explained [here](https://github.com/Benjol/SE-AutoReviewComments/issues/132#issuecomment-2256025023), AutoReviewComments is effectively abandonware. so this fork is irrelevant and therefore archived.

Tailored for [Blender Stack Exchange](https://blender.stackexchange.com/) to be used with [SE-AutoReviewComments: AutoReviewComments - Pro-forma comments for SE](https://github.com/Benjol/SE-AutoReviewComments?tab=readme-ov-file#installation)

Install the above extension/userscript. Then you can either import the comments in markdown format from the readme, or [remote](https://stackapps.com/questions/2116/autoreviewcomments-pro-forma-comments-for-se/3281#3281) the raw [comments.js](https://raw.githubusercontent.com/L0Lock/BlenderSE-ProFormaComments/master/comments.js) file so to not have to constantly import manually at each update.

> [!Note]
> 
> Yes the official documentation asks for a .jsonp, but users have reported the remote import to fail unless using .js extension.


> [!Warning]
> It seems that getting remote is bugged out anyway:
> [Importing remote, or any JSON · Issue #132 · Benjol/SE-AutoReviewComments](https://github.com/Benjol/SE-AutoReviewComments/issues/132#issuecomment-2249041323)

## Contributing

While technically you need to edit only one file, the following steps allow to automatically update the readme. In the future, ideally it should also allow adding entries from either json or md formats as the contributor wishes.

> [!Note]
> Requires Python, and some familiarity with JSON formatting ;)

- Clone or Download the repository

- Edit `generation/comments_contrib.js` (see bellow guidelines)

- Once done, open command line in repository root
  
  - Run `python generate.py` to update comments.js  
    It will ask you if you want to alphabetically sort the json entries first. And if you want to update the readme. This is to save time when quick testing, please do run these before sending a Pull Request.
  
  - If encountering issues, run `python generate.py --debug` and post the generated `debug.log` file in a [bug report](https://github.com/L0Lock/BlenderSE-ProFormaComments/issues).

### Entries Guidelines

Here are some templates to add new entries:

```json
  // Finish every {} with a comma, except the last one of the list!
  // Templates of Question only, Answer only, and common messages.
    {
        "name": "[Q]name",
        "description": "Message."
    },
    {

        "name": "[A]name",
        "description": "Message."
    },
    {

        "name": "name",
        "description": "Message."
    },
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

## Content:

### English Please

English is mandatory language for the site. If you are not comfortable writing in English feel free to use any online translation service.

### Link: Blend Exchange

[blend-exchange.com](https://blend-exchange.com/)

### Link: Blender Artists

[Blender Artists Forum](https://blenderartists.org/)

### Link: EXR Color Management

[EXR Color Management](https://blender.stackexchange.com/a/315682/53447)

### Link: FBX Materials have no textures

[Why FBX Materials have no textures](https://blender.stackexchange.com/questions/57531/fbx-export-why-there-are-no-materials-or-textures)

### Link: Guidelines for faster render

[Guidelines for faster render](https://blender.stackexchange.com/questions/52559/how-to-render-a-scene-faster-in-cycles?r=Saves_UserSavesList)

### Link: Image formats and Video Codecs comparison - performance and compression

[Image formats and Video Codecs comparison - performance and compression](https://blender.stackexchange.com/questions/148231/what-image-format-encodes-the-fastest-or-at-least-faster-png-is-too-slow?r=Saves_UserSavesList)

### Link: Texture support in 3d exchange formats

[Texture support in 3d exchange formats](https://blender.stackexchange.com/questions/57531/fbx-export-why-there-are-no-materials-or-textures?r=Saves_UserSavesList)

### Link: Transparency and Alpha Issues

[Transparency and Alpha Issues](https://blender.stackexchange.com/a/222893/53447)

### Operator Scripting

Operators in bpy.ops are [for interactive use through the UI and should be avoided in scripts](https://blender.stackexchange.com/questions/2848/why-avoid-bpy-ops/2850#2850) because they depend on context. Using them through scripts may yield unexpected results at best, or fail entirely at worst. Manipulate data directly from bpy.data instead.

### [A]AI-generated Answer

Was this generated by artificial intelligence, chat assistants or otherwise with help from large language models? According to our [site rules](https://blender.stackexchange.com/help/gen-ai-policy) decided by the community through [democratic voting](https://blender.meta.stackexchange.com/questions/3071), we do not currently accept answers generated by artificial intelligence, chat assistants or otherwise with help from large language models. If that is the case here, we'd kindly ask you to either make an answer on your own, or delete it so as not to infringe the rules. Thanks for understanding

### [A]Comment answer

Hello and welcome. This site is not a regular forum, the answer section is reserved exclusively for answering the OP question. To ask for clarification, post comments or replies please use the comments section instead. If you have the same problem or a different question please use the [Ask Question](https://blender.stackexchange.com/questions/ask) button at the top right. If you want to add additional information or further developments, use the edit button below the original post instead. This post may be removed or converted to a comment.

### [A]Link-only answer

This is not a regular forum, according to site rules [links to answers are not answers](https://blender.meta.stackexchange.com/questions/2382) if the link goes missing your answer becomes an empty shell without content. Answers should be substantial and stand on their own without relying on external data like links, videos or images. Instead of having users go through external links, either transcribe essential parts of the process here, linking the source, or posts these in the comments section instead.

### [A]Low Quality Answer

This site is not a regular forum, answers should be substantial, stand on their own, and thoroughly explain the solution and required steps. One liners and short tips and sole links rarely make for a good answer. If you can, [edit] your post and provide some more details about the procedure and how it works, perhaps add a few [images](https://blender.meta.stackexchange.com/questions/963) illustrating some steps and final result. See [How to write a good answer?](https://blender.stackexchange.com/help/how-to-answer), otherwise it may be converted to a comment.

### [A]Not an answer

This site is not like a traditional forum, it is a question and answers site. The pages are divided in two main sections: a single question and many possible answers to it. And you can comment any question or answer for extra discussions about them. Take the [tour] to understand how to make better use of this site.

### [Q]ALL CAPS OKTOBERFEST

Please don't write in all caps, it is the online equivalent of shouting, is [harder to read](https://en.wikipedia.org/wiki/All_caps#Readability) and is [considered rude](https://en.wikipedia.org/wiki/All_caps#Computing).

### [Q]Accept the Answer

If the answer solved your problem, please mark it as accepted [using the ✔️ button on the upper left corner](https://i.sstatic.net/viamd.png)? Feel free to also upvote it using ⬆️ just above. This helps others know that the question has been answered sufficiently, and gives the user who answered some more reputation.

### [Q]Bug Report

If you found a bug please report it to the official bug tracker. For Blender, use the menu Help > Report a Bug. For addons or extensions, go in Preferences > Addon, and click the documentation or bug button available in the addon's details. Also read: [Best place to put bug reports?](https://blender.stackexchange.com/a/173685)

### [Q]Edit instead of Comments

Instead of comments, please use the [edit] link at the bottom of your question (https://i.sstatic.net/vHwEx.png) to add information to your post.

### [Q]Experimental Software

Troubleshooting temporary issues with unfinished, under development or experimental versions of software are off-topic. These transitory questions are unlikely to be useful in the future because of the temporary and unreliable nature of experimental software, rendering their long term value low, and making them unappealing for a knowledge database site.

### [Q]Insert Code

Please do not post images or screenshots of your code, console or error messages. Instead copy-paste the actual text into your post using [proper code tags](https://meta.stackexchange.com/editing-help#code), so it can be clearly readable, indexed and searched for, and other users trying to help don't have to type it by hand themselves which is error prone and time consuming.

### [Q]Insert File

Please consider [sharing your .blend file](https://blender.meta.stackexchange.com/a/3051/53447) so that others can inspect it and give a more relevant answer.

### [Q]Insert Images

Please use the [built in tools](https://meta.stackexchange.com/questions/75491) to add images to your question. Use an image editor, or online optimizer, if you must resize an image. You can help those who would answer your question if all the information is displayed as part of the question and not as links.

### [Q]Lack of details

Hello and welcome. As it stands this question is not answerable at the moment for lack of essential details to understand the issue. Remember only you have access to your scene, only you know your exact setup, settings and what steps you took to arrive where your are now. Please describe in detail what your issue is, possibly supported by some [accompanying screenshots](https://meta.stackexchange.com/questions/75491) with the [edit] button under the question or even [share your file](https://blender.meta.stackexchange.com/a/3051/53447). Editing will automatically put it up for review so it can be reopened.

### [Q]Meta question

For Questions about this site, the network, moderation, rules and how they work, please use [Meta](https://blender.meta.stackexchange.com) instead.

### [Q]Multiple Questions

Hello and welcome. Please don't ask more than one question per post. Use the [edit] link below your post, to break this into multiple posts so that each focuses on a single issue. Make as many separate questions as necessary.

### [Q]Multipost

Please don't ask the same question multiple times. If you are not getting answers, or the answers don't help, or you wish to add new information, then edit your original post with more information and detailing what you have tried that is not working. Read: [What should I do if no one answers my question?](https://blender.stackexchange.com/help/no-one-answers)

### [Q]Opinon / Critique based question

This site works best for focused questions and answers and is not meant for opinions or open ended discussions. You can use the forums at https://blenderartists.org/, there are sections for focused critique and work in progress. To understand how to make better use of this site please take the [tour] and read through the [help] center section, particularly [How do I ask a good question?](https://blender.stackexchange.com/help/how-to-ask) and [What types of questions should I avoid asking?](https://blender.stackexchange.com/help/dont-ask).

### [Q]Paid addons

While questions about third-party addons can be answered here, be aware that obscure or paid addons are mechanically less likely to find an answer since we can't expect volunteers to go through unreasonable steps like spending money, installing extra software or giving away private information in subcribtion forms for the sake of an answer.

### [Q]Pictures or files with not enough text

While files, images, and external links to videos or .blend files may be helpful additions to questions they should not remain the only way to obtain information about your issue. Don't make understanding your question rely on downloading a file or visiting an external site. Use the builtin tools to [upload images](https://meta.stackexchange.com/questions/75491) or [gifs](https://blender.meta.stackexchange.com/questions/963), besides **thoroughly** explaining the problem in **written** form so it can be searched for and indexed thus helping future users find it.

### [Q]Question Too Broad

Hello and welcome. As it stands this question is too broad to be answerable without requiring an extensive tutorial or description. You should show efforts towards reaching your goal, describing what you have tried and why it failed, so we don't risk recommending something you already know. The scope should also focus on a particular step you encountered an issue with. Describing the whole procedure from start to finish would be too lengthy to explain, and is beyond the goal of this site. If you could [edit] your post to focus on where you are stuck we can vote to reopen it.

### [Q]Request Art Critique

This question is considered off topic here and was put on hold for being subjective and attracting opinion based answers, because there are no "right" or "wrong" answers and every suggestion is equally valid. For art critique, tips, artistic input, or other opinion based suggestions it is best to ask over at [Blender Artists Forum](https://blenderartists.org/) or similar forums. If you can rephrase it to focus on objective questions or solving specific issues feel free to [edit] it so it can be reopened.

### [Q]Request Feature / Development

This is Q&A site run by volunteers, we are not programmers nor in any way associated with the Blender Foundation, decision making nor development process of the software. For suggestions and feature requests use https://blender.community/c/rightclickselect or https://blenderartists.org. Before doing so consider that ideas are a dime-a-dozen, what we lack is manpower. Every single one of the millions of users have their own long list of personal wishes and desires, while comparatively very few people have the knowledge and inclination to actually implement them.

### [Q]Request Resources

Asking for links to resources about X is considered off topic here, asking directly about X is encouraged though. If you can rephrase your question to focus on the specific difficulties you are encountering, rather than point you to some site, please [edit] your post so it can be reopened. As it stands it is not a good fit for this site.

### [Q]Request Tutorial

[Requests for tutorials are considered off topic here](https://blender.meta.stackexchange.com/questions/1). If it requires a full tutorial the question is either [too broad and needs to be narrowed down](https://blender.meta.stackexchange.com/questions/62) to a more specific issue; or it can be solved with a simple web search which you can easily do yourself. Please don't post another question. If you could you rephrase the current one to read more like a direct inquiry about your issue, rather than pointing you to a link, you can [edit] it so it can be reopened.

### [Q]Request comissions

This is not a regular forum, we are a question and answer site aimed at providing users with assistance along the way, rather than solve the issues for them or present ready made solutions. For commissioning work, job posts or hiring someone, there is a paid work section at [Blender Artists Forum](https://blenderartists.org). Otherwise rephrase your question so it shows your efforts towards solving the issue, rather than ask for someone to do it for you, so it can be reopened.

### [Q]Request legal/licencing advice

This website is neither equipped nor legally qualified to give legal or licencing advice. And any ill advice could unintentionally pose a liability to both the user and the network. For official info see the [Blender Licensing Terms and Conditions](https://www.blender.org/about/license/) and the [FAQ about GNU GPL](https://www.blender.org/support/faq/#gnu-gpl)

### [Q]Solved

If you found a solution for your problem please write it on the answers section and mark it as accepted there. Read: [what does it mean when an answer is accepted?](https://blender.stackexchange.com/help/accepted-answer). Do not edit your question to mark it solved nor to include the solution

### [Q]Third-Party addons

As discussed [on Meta BSE](https://blender.meta.stackexchange.com/q/3043/53447): questions about third-party addons can be answered here if anyone knows the answer, because addons are integral to Blender’s functionality. We accept questions about them as long as they are within scope, excluding bug reports, network issues. With the caveat that questions about obscure or paid addons are mechanically less likely to find an answer.

### [Q]Title to broad

Please make the title of your question specific to the problem you are having and not just the general topic, see: [How do I ask a good question?](https://blender.stackexchange.com/help/how-to-ask).

### [Q]XY Problem

This sounds like the [XY Problem](https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem). Could you please clarify the underlying issue you're trying to solve (X) rather than the specific solution you're focusing on (Y)? This will help us better understand your needs and offer more relevant advice.
