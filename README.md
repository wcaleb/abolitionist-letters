# abolitionist-letters
Transcriptions of some of the abolitionist letters in the Boston Public Library's Internet Archive collection

## What is This?

In 2013, I published a [book on transatlantic abolitionists][book] that relied heavily on abolitionist letters in the Boston Public Library's [Antislavery Collection][bpl]. In the spirit of [open notebook history][onh], I am now making available many of the notes I took on these abolitionist letters.

I decided to share my partial transcripts and notes partly because, after completing my dissertation and book, the Boston Public Library began collaborating with the Internet Archive to put [digitized versions of their abolitionist letters online][bplscas].

The digitized antislavery collection makes it possible to do some limited data mining using the MARC records for each item, as I explained in a lesson for the [Programming Historian][ph]. However, most of the letters are manuscripts, and so it is not currently possible to search the full text of the letters. My hope is that open-sourcing my notes and transcriptions might seed a larger attempt to transcribe these letters so that richer mining of their contents will be possible. To that end, this repo provides an index of possible matches between my transcriptions and the letters that have currently been uploaded by the BPL to the Internet Archive.

[onh]: http://wcm1.web.rice.edu/open-notebook-history.html
[book]: http://www.amazon.com/Problem-Democracy-Slavery-Abolitionists-Transatlantic/dp/0807150185/
[bpl]: https://www.bpl.org/distinction/featured-collections/anti-slavery/
[bplscas]: http://archive.org/details/bplscas/
[ph]: http://programminghistorian.org/lessons/data-mining-the-internet-archive

## Disclaimers

My decisions about which letters to transcribe---and how much of an excerpt to include---were driven by my particular research interests for my dissertation and book. As a result, I did not transcribe every letter I looked at. Sometimes I just included a brief note of the date, author, and recipient of a letter. Sometimes I included notes, instead of a direct transcription, and I have tried to indicate that in my notes. But as in any such case, readers should use these notes and transcriptions with caution and check the original letters themselves. 

I originally took my notes in a single Microsoft Word, so to create plain text versions of my notes for this repo, I had to convert that document using [Pandoc](http://pandoc.org), and then use UNIX tools to attempt to burst the file so that each letter was in its own plain text file. Since this created thousands of small files, I have not been able to check to ensure that there were no errors in the splitting process, which means some of the transcription files may erroneously contain multiple letters or none at all.

Finally, right now this repo is a "proof of concept" sort of project, so it does not yet include *all* the notes and transcriptions I made, but only a small selection of them.

## How Do I Use These?

If you want to download, to your own machine, the MARC records for all of the letters that are currently in the BPL's Internet Archive antislavery collection, you can use the `get-bpl-marcs.py` script, but make sure you know what you're doing and read [my Programming Historian lesson][ph] first.

Once you have the MARCs on your machine, the `match-transcriptions.py` script will attempt to match up XML records with my partial transcriptions, included in the `transcriptions/` directory. The filenames of my transcriptions correspond to the call numbers of the items at the BPL, which are also included (in a slightly different format) in the MARC XML records. So the script attempts to perform some rough matching on the call numbers, but it's a work in progress and I'd welcome help from those who might have better suggestions about how to check for matches.

The `transcription-index.csv` file contains URLs for Internet Archive items that I believe I may have a transcription of. Each row also contains the (possible) author and recipient of the letter, scraped from the MARC XML record associated with the potentially matching Internet Archive item. To check manually if they do match, you can go to the URL, and then compare what you find there to the corresponding file found in the `transcriptions/` directory.

For example, you can check to see if [this transcription](https://github.com/wcaleb/abolitionist-letters/blob/master/transcriptions/Ms.A.9.2.23.75) matches [this original manuscript](https://archive.org/details/lettertodearfrie00alle). (See page two of the manuscript for the excerpt I transcribed.)

Please [contact me](http://wcm1.web.rice.edu) or file an issue if you have any problems or questions.
