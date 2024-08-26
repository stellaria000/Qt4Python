import People

BirthdayParty {
    id: theParty
    HappyBirthdaySong on announcement {name: theParty.host.name}
    onPartyStarted: (time)=> {console.log("THIS PARTY STARTED ROCKIN' AT "+time);}

    host: Boy {
        name: "Bob Jones"
        shoe_size: 12
    }

    Boy {
        name: "Leo Hodges"
        BirthdayParty.rsvp: "2009-07-06"
    }

    Boy {
        name: "Jack Smith"
    }

    Girl {
        name: "Anne Brown"
        BirthdayParty.rsvp: "2009-07-01"
    }
}