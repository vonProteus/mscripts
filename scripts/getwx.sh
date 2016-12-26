#!/bin/bash 

NAMETAG=$1
WXNAME=$2
WXAPIKEY=$3

WXAPRS="http://api.aprs.fi/api/get?name=$WXNAME&apikey=$WXAPIKEY&format=xml&what=wx"
WXFILE="/tmp/aprs.wx.xml"
TIMECASH=$(( 60 * 60 * 5 )) # 5  minut


NOW=$(date -u +%s)
LASTTIME=$(xmlstarlet sel -t -v "/xml/entries/entry/time" $WXFILE )

if (( $NOW - $TIMECASH > $LASTTIME +1 ))
then
	wget $WXAPRS -O $WXFILE
fi

xmlstarlet sel -t -v "/xml/entries/entry/$NAMETAG" $WXFILE
