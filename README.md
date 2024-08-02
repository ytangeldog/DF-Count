# Don't Forget (Connected/Classic) Players Counter

## Introduction
This is a website that checks the number of players currently playing Don't Forget every 5 minutes and logs them in a `stats.txt` file so it can be used later to make graphs. It was intended to be used as a tag in the 42 Discord bot by displaying a website URL embed showing the number of current players in Don't Forget.

## How it Works
The website fetches data from the [GameMaker Server Status website](https://status.gamemakerserver.com/) and stores it in the website's metadata, so it can appear as an embed in Discord. Since this is a static page, GitHub Actions are used to update the metadata every 5 minutes. The project also includes a Python file that generates weekly and monthly graphs using the data from the `stats.txt` file.

## How to Use it in the 42 Discord Bot
You can use the following code in your tag:

```python
{oneline:
{!!description A Tag made by ytangeldog that checks current players in Don't Forget Games

**(+t dfonline)** Checks players in Don't Forget Connected
**(+t dfonline classic)** Checks players in Don't Forget Classic
**(+t dfonline [optional:classic] stats)** Shows a weekly graph of players in Don't Forget Connected or Classic
**(+t dfonline [optional:classic] stats month)** Shows a monthly graph of players in Don't Forget Connected or Classic}
{set:randomshit;{choose:1;2;3;4;5;6;7;8;9;10;}{choose:1;2;3;4;5;6;7;8;9;10;}{choose:1;2;3;4;5;6;7;8;9;10;}{choose:1;2;3;4;5;6;7;8;9;10;}{choose:1;2;3;4;5;6;7;8;9;10;};}\n
{when:{arg1};eq;classic;
    {when:{arg2};eq;stats;
        {when:{arg3};eq;month;
            [The Graph updates every month](https://ytangeldog.github.io/DF-Count/graph2.png?lol={randomshit})
        ;
            [The Graph updates every week](https://ytangeldog.github.io/DF-Count/graph.png?lol={randomshit})
        ;}
    ;
        [The Embed only updates every 7 minutes, if you want to know the current players playing now then go to the website](https://ytangeldog.github.io/DF-Count?lol={randomshit})
    ;}
;
    {when:{arg1};eq;stats;
        {when:{arg2};eq;month;
            [The Graph updates every month](https://ytangeldog.github.io/DF-Count/dfconnected/graph2.png?lol={randomshit})
        ;
            [The Graph updates every week](https://ytangeldog.github.io/DF-Count/dfconnected/graph.png?lol={randomshit})
        ;}
    ;
        [The Embed only updates every 7 minutes, if you want to know the current players playing now then go to the website](https://ytangeldog.github.io/DF-Count/dfconnected?lol={randomshit})
    ;}
;}
;}
```
This code provides various commands to check the current number of players in Don't Forget Connected and Don't Forget Classic, as well as access to weekly and monthly player count graphs. (to know how to use it, type `+t info "tagname"`)
