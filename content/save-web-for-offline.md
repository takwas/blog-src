Title: wGetting Them All!
Date: 2016-01-28 17:00
Modified: 2016-01-29 22:00
Tags: wget, httrack, download, offline, save, website, internet, planet
Slug: save-web-for-offline
Summary: You can save the entire contents of a website or blog for offline referencing.




If you are in a location with internet connection issues, or limited by the amount of bandwidth you can afford, then there are ways you can leverage the resources that are useful to you on the web.

Some websites or blogs have content arranged in order of chapters that I like to read in that order. And some others just appeal to me as troves of useful content that I would want to keep within easy reach. The challenge with this is that there are times when I have no active internet subcscription or connection, making such resources unavailable to me.

Interestingly, it is possible for me to keep an entire website offline. With the help of some of tools, I could download the site for offline reading! This is **particularly workable with static sites** that have no interaction with the backend, other than delivering static pages to us -- so don't think of doing this with Facebook, or Quora. **:)**

<br/>

There are two ways I do this:

1. I use the __[HTTrack Website Copier](http://www.httrack.com/)__ software, which is available cross platform; and 
2. __[wget](http://linux.die.net/man/1/wget)__, I learnt about this one recently.

I also use this approach to download documentations for offline reference, since they're mostly static.

The most current version of HTTrack supports resumption of broken downloads. This is also built into wget, which is an old Linux tool.

One issue I have observed with the latter, however, is that it doesn't seem to get the CSS style files accordingly; therefore, you may have aesthetic issues with it. I have not had this problem with HTTrack.

HTTrack is multiplatform supported. There are versions for Android, Windows, and Linux, [downloadable here](http://www.httrack.com/page/2/)

The typical command for wget is:

` $ wget --continue --wait=20 --limit-rate=20K -r -p -U [BROWSER] [URL_TO_SITE]`

For example:

` $ wget --continue --wait=20 --limit-rate=20K -r -p -U Mozilla http://takwas.github.io/`
