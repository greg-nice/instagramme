from app.models import db, Post
import datetime

# Adds a demo user, you can add other users here if you want
def seed_posts():

    p1 = Post(
        user_id=2, description="""There was something almost otherworldly about this vantage point on Round Island, Alaska—the rich green water, the fissures in the ancient rocks, the surfacing of walrus, like creatures from the moon. Pacific walrus are known to have rested on this island every summer for thousands of years, and it took millions more for them to evolve into the highly specialized, sensitive, Arctic clam-eater they are today.

        Contemplating the vast timescales of evolution often evokes, for me, a wonderful and comforting sense of insignificance. But it's also powerful motivation to work toward preserving the animals and ecosystems that have existed far back into deep time—which need our attention to survive into the future.""", createdAt=datetime.datetime(2021, 12, 6), updatedAt=datetime.datetime(2021, 12, 6))

    p2 = Post(
        user_id=2, description="""Chile. This year ought to be the “super year” for nature, the one where we collectively agree on the unacceptable risk we have taken by becoming totally out of balance with nature. The path forward is simple, though it will take all of us working together for a better future. We need to protect at least 30% of land and ocean by 2030 in order to preserve biodiversity, address climate change, and support our growing population.""", createdAt=datetime.datetime(2021, 12, 5), updatedAt=datetime.datetime(2021, 12, 5))

    p3 = Post(
        user_id=2, description="""Firefighters with Cal Fire conduct an operation to contain the Dixie fire south of Highway 44 in Lassen National Forest, on August 27. The fire started on July 13. At the time of this image, on October 2, it had burned roughly 965,000 acres (400,000 ha) and was 94% contained. Now it's fully secured. Shot on assignment with the help of a grant from the National Geographic Society.""", createdAt=datetime.datetime(2021, 12, 4), updatedAt=datetime.datetime(2021, 12, 4))
    p4 = Post(
        user_id=2, description="""A lion in Uganda’s Queen Elizabeth National Park grips the trunk of a large fever tree. Lions in this part of Africa have a unique habit of climbing large fig, acacia, and euphorbia trees, a cultural behavior that's common across the prides. Every day around 7 in the morning, the prides find a tree and climb. The cited reasons for this behavior include increasing their view of the landscape to escaping biting flies! If you think of a better one, leave a comment.
        """, createdAt=datetime.datetime(2021, 12, 4), updatedAt=datetime.datetime(2021, 12, 4))
    p5 = Post(
        user_id=2, description="""A basking shark cruises along the west coast of Scotland. After locating a plankton patch, this giant opened its mouth and blasted right through it. The white gill arches contain rakers—structures that snag plankton from water passing through its mouth. Unlike many other species of filter feeder able to pump water through gill rakers, basking sharks feed passively. This means they must swim to eat. Given their size, they need to do a lot of eating—and therefore a lot of swimming. It’s estimated they can filter two million liters (500,000 gallons) of water per hour!
        """, createdAt=datetime.datetime(2021, 11, 30), updatedAt=datetime.datetime(2021, 11, 30))
    p6 = Post(
        user_id=2, description="""A hike to the ice caves of Longyearbreen, a glacier in Svalbard, Norway, feels like time travel. The air bubbles trapped in this ice contains air from a thousand years ago. Due to climate change, Svalbard's glaciers lost their protection during the 1980s and have been melting ever since. Let’s act to protect this delicate Arctic environment—and our future.""", createdAt=datetime.datetime(2021, 11, 28), updatedAt=datetime.datetime(2021, 11, 28))
    p7 = Post(
        user_id=2, description="""It's a sign of physical prowess, health, and virility. The bushier, darker, and more lustrous the mane, the stronger the signal that its owner is a male lion to be reckoned with. They may not be the most convenient accessory amid insects and sweltering heat, but luxuriant manes do have distinct advantages. They attract potential mates with the promise of superior genes, and they intimidate rivals and foes by indicating fitness and fighting ability. And this maned hunter is certainly proving his chops.""", createdAt=datetime.datetime(2021, 11, 21), updatedAt=datetime.datetime(2021, 11, 21))
    p8 = Post(
        user_id=2, description="""
        I'm in the field in Vostok, Southern Line Islands, on a @natgeopristineseas expedition. This is what coral reefs were like before we depleted them by overfishing and from the impact of global warming. But we know that protection from damaging activities allows marine life to bounce back. Kiribati protected the Southern Line Islands. If the rest of the world would do the same with vital places in their waters, we could achieve the global goal of 30% of the ocean protected by 2030
        """, createdAt=datetime.datetime(2021, 11, 17), updatedAt=datetime.datetime(2021, 11, 17))
    p9 = Post(
        user_id=2, description="""The month of October in Acadia National Park was spectacular. When the wind died at dusk, the colorful trees reflected perfectly in the still waters of Upper Hadlock Pond. See more from this fall in Maine""", createdAt=datetime.datetime(2021, 11, 16), updatedAt=datetime.datetime(2021, 11, 16))

    p10 = Post(
        user_id=2, description="""Presenting the mysterious forest cobra, native to the central and western parts of Africa. It's the largest cobra species, with a length up to 3.1 meters (10 ft). I've also photographed the king cobra, which is much bigger but is the sole member of its own genus. The forest cobra is a capable swimmer and is often considered to be semiaquatic. My team and I searched the lowland forests and wet savanna habitats for this beautiful species during an assignment in Cameroon, and eventually we got lucky. It's a fast snake, with a reputation for being alert and sometimes nervous. Bites to humans are less common than for other African cobras due to various factors, though a bite from the forest cobra is indeed a life-threatening emergency. Ironically the lethal characteristics of snake venom are what make it valuable and sought after for use in medicinal treatments. The toxic components of snake venom have led to the development of remedies for heart disease, diabetes, and Alzheimer's. With a bit of luck, the forest cobra also may soon combat heart disease, without affecting the wild populations of the species.
        """, createdAt=datetime.datetime(2021, 11, 13), updatedAt=datetime.datetime(2021, 11, 13))

    p11 = Post(
        user_id=2, description="""Beyond the overt devastation that poaching wreaks on wild species, there are many other more subtle, more insidious impacts. In elephants, researchers are seeing growing evidence of harm—not only for population numbers but also in the animals’ very genetics. In some parts of the world, for example, ivory poaching appears to have triggered complex genetic changes that are driving a surge in tusklessness—a shift that may protect these iconic giants from poachers, but also unleash unknown ripple effects on their well-being and the health of ecosystems. The consequences of our intense exploitation of the natural world are vast and undeniable. The need for change and action has never been more urgent.
        """, createdAt=datetime.datetime(2021, 11, 14), updatedAt=datetime.datetime(2021, 11, 14))

    p12 = Post(
        user_id=2, description="""
        2021 has been declared the International Year of Caves and Karst. Cavers, researchers, and those who appreciate the underground will be promoting the beauty, wonder, and life beneath our feet. This is my world, a place where I truly feel at one with nature. Caves can help us to better understand not only this planet but others. Features in lava tubes like this one, called Grotta del Gelo on the flanks of Mount Etna, in Sicily, help educate us about potential life that may exist in extreme environments on other planets.
        """, createdAt=datetime.datetime(2021, 11, 12), updatedAt=datetime.datetime(2021, 11, 12))
#******************************NASA**************************
    p13 = Post(
        user_id=3, description="""Down for a dip in the Cosmic Reef?

        Nicknamed the Cosmic Reef because it resembles an undersea world, this is a vast star-forming region in the Large Magellanic Cloud, a satellite galaxy of the Milky Way!

        The sparkling centerpiece of the orange nebula (NGC 2014) is a grouping of bright, hefty stars, each 10 to 20 times more massive than our Sun. By contrast, the seemingly isolated blue nebula at upper right (NGC 2020) has been created by a solitary mammoth star 200,000 times brighter than our Sun!

        Released in April 2020 to celebrate @NASAHubble’s 30th anniversary, the Cosmic Reef showcases the beauty and mystery of space in this complex image of starbirth.""", createdAt=datetime.datetime(2021, 11, 19), updatedAt=datetime.datetime(2021, 11, 19))
    p14 = Post(
        user_id=3, description="""A blue sunset on the Red Planet

        Our Perseverance Mars rover has taken its first picture of a sunset! This image was captured on Nov. 9, 2021, by the rover's Mastcam-Z camera system on the 257th Martian day, or sol, of the mission.

        While this is the first sunset imaged by Perseverance, Our robotic explorers have been looking up at the Sun from the surface of the Red Planet since the 1970s. Vikings 1 and 2; the Pathfinder and Phoenix landers; Spirit, Opportunity and Curiosity rovers have sent back sunrise and sunset scenes.

        Martian sunsets typically stand out for their distinctive blue color. Fine dust in the atmosphere permits blue light to penetrate the atmosphere more efficiently than colors with longer wavelengths. But this sunset looks different: less dust in the atmosphere resulted in a more muted color than average. The color has been calibrated and white-balanced to remove camera artifacts.""", createdAt=datetime.datetime(2021, 11, 22), updatedAt=datetime.datetime(2021, 11, 22))
    p15 = Post(
        user_id=3, description="""Did someone order a dark ‘n stormy? 🌌

        About 1,400 light-years from Earth lies the largest star-forming cluster in the constellation of Orion, the Flame Nebula. The dark and dusty heart of nebula, pictured here, is where star a cluster resides, mostly hidden from view.

        Nearby (but not visible in this image), is the bright star Alnitak, the easternmost star in the Belt of Orion. Radiation from Alnitak ionizes the Flame Nebula’s hydrogen gas. As the gas begins to cool from its higher-energy state to a lower-energy state, it emits energy in the form of light, causing the visible glow behind the swirled wisps of dust.""", createdAt=datetime.datetime(2021, 11, 23), updatedAt=datetime.datetime(2021, 11, 23))
    p16 = Post(
        user_id=3, description="""Our Curiosity Mars rover was thinking of you and decided to send you a postcard of its most recent perch on the side of Mars’ Mount Sharp. Keeping in touch with loved ones is important!

        Curiosity captures a 360-degree view of its surroundings with its black-and-white navigation cameras each time it completes a drive. To make the resulting panorama easier to send to Earth, the rover keeps it in a compressed, low-quality format. But when Curiostiy saw the view from its most recent stopping point, the scene was just too pretty not to capture it in the highest quality that the navigation cameras are capable of.

        The beauty of the landscape was so inspiring, in fact, that the mission team decided to add a little flair: they combined two versions of the black-and-white images from different times of the day and added colors to create a rare postcard from the Red Planet.""", createdAt=datetime.datetime(2021, 11, 25), updatedAt=datetime.datetime(2021, 11, 25))
    p17 = Post(
        user_id=3, description="""We're on our way to nudge an asteroid!

        Our DART spacecraft lifted off at 1:21 a.m. EST (6:21 UTC) this morning, beginning its 10-month journey to the small "moonlet" Dimorphos. Late next year, the vending machine-sized ship will smash into Dimorphos at more than 15,000 miles an hour (24,000 kph), altering its orbit very slightly around the larger asteroid Didymos.

        Dimorphos does not pose a threat to Earth, either before or after DART's impact, but the data we collect from DART's collision will help us design spacecraft to deflect any future asteroids or near-Earth objects that ever threaten our home planet. Designed by @JohnsHopkinsAPL, DART lifted off on a @SpaceX Falcon 9 rocket from @Vandenberg_SFB in California.""", createdAt=datetime.datetime(2021, 11, 24), updatedAt=datetime.datetime(2021, 11, 24))
    p18 = Post(
        user_id=3, description="""Mounded, luminous clouds of gas and dust glow in this @NASAHubble image of a Herbig-Haro object known as HH 45. Herbig-Haro objects are a rarely seen type of nebula that occurs when hot gas ejected by a newborn star collides with the gas and dust around it at hundreds of miles per second, creating bright shock waves.

        HH 45 is located in the nebula NGC 1977, which itself is part of a complex of three nebulae called The Running Man. These three nebulae are reflection nebulae, which means that reflect light from nearby stars instead of emitting light on their own, like a streetlight illuminating fog.""", createdAt=datetime.datetime(2021, 11, 27), updatedAt=datetime.datetime(2021, 11, 27))
    p19 = Post(
        user_id=3, description="""
        TFW your office is outer space.

        Here are photos of @JAXAJP astronaut Aki Hoshide and @EuropeanSpaceAgency astronaut @Thom_Astro from last weekend’s spacewalk to prepare upgrades for the @ISS solar arrays. The duo finished all spacewalk tasks in just under 7 hours while orbiting 263 miles (421 kilometers) above, bringing the concept of """, createdAt=datetime.datetime(2021, 9, 16), updatedAt=datetime.datetime(2021, 9, 16))
    p20 = Post(
        user_id=3, description="""For the first time, astronomers may have detected an exoplanet candidate outside of the Milky Way galaxy. Exoplanets are defined as planets outside of our solar system. All other known exoplanets and exoplanet candidates have been found in the Milky Way, almost all of them less than about 3,000 light-years from Earth.

        This new result is based on transits, events in which the passage of a planet in front of a star blocks some of the star's light and produces a characteristic dip. Researchers used our @NASAChandraXray Observatory to search for dips in the brightness of X-rays received from X-ray bright binaries in the spiral galaxy Messier 51, also called the Whirlpool Galaxy (pictured here). These luminous systems typically contain a neutron star or black hole pulling in gas from a closely orbiting companion star. They estimate the exoplanet candidate would be roughly the size of Saturn, and orbit the neutron star or black hole at about twice the distance of Saturn from the Sun.

        This composite image of the Whirlpool Galaxy was made with X-ray data from Chandra and optical light from our @NASAHubble Space Telescope.""", createdAt=datetime.datetime(2021, 12, 5), updatedAt=datetime.datetime(2021, 12, 5))
    p21 = Post(
        user_id=3, description="""Have you ever seen a total solar eclipse? How about seeing a total solar eclipse FROM SPACE?

        Our robotic and human explorers are here to help. On Dec. 4, 2021, the Deep Space Climate Observatory (DSCOVR) spacecraft captured the Moon's shadow as it passed over Antarctica, home to penguins and a handful of scientists. Shaped like a cone extending into space, the shadow has a circular cross-section most easily seen during a solar eclipse. People in parts of Namibia, South Africa, New Zealand, and the Falkland Islands were treated to a partial eclipse.

        How about seeing it from another perspective? Astronaut Kayla Barron snapped images of the eclipse from inside the International Space Station (@ISS). Visible in the foreground is a Russian segment of the orbiting laboratory.

        A solar eclipse happens when the Moon moves between the Sun and Earth, casting a shadow on Earth, fully or partially blocking the Sun’s light in some areas. For a total solar eclipse to take place, the Sun, Moon, and Earth must line up exactly.

        A joint NASA-@NOAA observatory, DSCOVR orbits about a million miles from Earth and takes a new picture of Earth every two hours with its camera called EPIC – the Earth Polychromatic Imaging Camera. Launched in 2009, DSCOVR monitors changes in the solar wind and provides space weather forecasts and alerts for solar storms that could temporarily disrupt power grids and GPS.
        """, createdAt=datetime.datetime(2021, 12, 6), updatedAt=datetime.datetime(2021, 12, 6))
    p22 = Post(
        user_id=3, description="""One ring to rule them all? Not on Saturn!

        Our Cassini spacecraft made 294 orbits around Saturn over 13 years before ending its mission on the ringed planet on Sept. 15, 2017.

        Cassini opened our eyes to the mysteries of Saturn, and to Saturn's moons containing methane rivers, jets of ice and gas blasting material into space, and a liquid water ocean that may harbor the ingredients for life.

        This artist rendering shows a wondrous view of Cassini orbiting the ringed planet.""", createdAt=datetime.datetime(2021, 9, 10), updatedAt=datetime.datetime(2021, 9, 10))
    p23 = Post(
        user_id=3, description="""This complex nebula is filled with glowing gases, lanes of dust, and stars of all ages—but what interests astronomers the most is what ISN'T there. One of its most distinctive features is the dark, starry gap called a “superbubble,” visible in this @NASAHubble image in the upper central region.

        The hole is about 250 light-years wide and its presence is still something of a mystery. Stellar winds expelled by massive stars in the bubble's interior may have driven away the gas, but this is inconsistent with measured wind velocities in the bubble. Another possibility, since the nebula is filled with massive stars that would expire in titanic explosions, is that the expanding shells of old supernovae sculpted the cosmic cavern.""", createdAt=datetime.datetime(2021, 11, 13), updatedAt=datetime.datetime(2021, 11, 13))
    p24 = Post(
        user_id=3, description="""Ready for a grand tour? Our Hubble Space Telescope completed its annual view of the outer planets, revealing both extreme and subtle changes to these distant worlds. In order, we see Jupiter, Saturn, Uranus (no jokes), and Neptune.

        Want to know what Hubble discovered? Head over to the @NASAHubble page.""", createdAt=datetime.datetime(2021, 11, 18), updatedAt=datetime.datetime(2021, 11, 18))

    p25 = Post(user_id=4, description='Felt like this stock photo deserved a dreamy version.', createdAt=datetime.datetime(2020, 6, 25), updatedAt=datetime.datetime(2020, 6, 25))
    p26 = Post(user_id=4, description="""Last chance to gain access to my exclusive Facebook group that goes live tomorrow!

Those of you who get in will get a lifetime access to the group where I'll be teaching everything I learned over the years - FOR FREE. It's a one time opportunity since starting tomorrow the group will be accesible only for my paid course students.
For a chance to get in, tag one of your friends in the comments and I'll randomly pick 2 of you tomorrow. It's a chance for you to learn EVERYTHING I know. (The group will be updated with valuable content on a daily basis.) Good luck!""", createdAt=datetime.datetime(2020, 6, 26), updatedAt=datetime.datetime(2020, 6, 26))
    p27 = Post(user_id=4, description="""How close fantasy actually is to reality, how little does it take for the whole world to change forever?""", createdAt=datetime.datetime(2020, 8, 26), updatedAt=datetime.datetime(2020, 8, 26))
    p28 = Post(user_id=4, description='Louvre', createdAt=datetime.datetime(2016, 4, 25), updatedAt=datetime.datetime(2016, 4, 25))
    p29 = Post(user_id=4, description='', createdAt=datetime.datetime(2016, 6, 14), updatedAt=datetime.datetime(2016, 6, 14))
    p30 = Post(user_id=4, description=""""Under the weather" is now available""", createdAt=datetime.datetime(2021, 4, 16), updatedAt=datetime.datetime(2021, 4, 16))
    p31 = Post(user_id=4, description="""Really excited to put this one on my feed. Huge thank you to Netflix for partnering with me regarding the release of the new Netflix horror series - Midnight Mass. Got to see the show early and really enjoyed it. Would definitely recommend it! So here's a little 8thdamon spin on the series.""", createdAt=datetime.datetime(2021, 10, 2), updatedAt=datetime.datetime(2021, 10, 2))
    p32 = Post(user_id=4, description="""8thdamon, Paris, France 2021.""", createdAt=datetime.datetime(2021, 10, 5), updatedAt=datetime.datetime(2021, 10, 5))
    p33 = Post(user_id=4, description="""Bitchin.""", createdAt=datetime.datetime(2018, 8, 25), updatedAt=datetime.datetime(2018, 8, 25))
    p34 = Post(user_id=4, description='Framed prints of all my photos will be available for purchase soon', createdAt=datetime.datetime(2017, 8, 18), updatedAt=datetime.datetime(2017, 8, 18))
    p35 = Post(user_id=4, description="""Created this edit in a little more than half an hour using just the enlightphotofox app (available on iOS - link is in the bio if you wanna try it). 👩🏼‍🚀🌎🧻 It's been a few years since I tried making these on my phone and it was really clumsy, apps were not comfortable to use at all and the effects looked cheap, now I couldn't believe how far layer editing has come on phones. It's so easy to control each layer by itself now, adding blur to each layer separately to control the depth of my edit as well.
The time we live in is just amazing!""", createdAt=datetime.datetime(2020, 5, 19), updatedAt=datetime.datetime(2020, 5, 19))
    p36 = Post(user_id=4, description='Dreamy Cappadocia', createdAt=datetime.datetime(2020, 5, 23), updatedAt=datetime.datetime(2020, 5, 23))



    p37 = Post(user_id=5, description='', createdAt='2021, 1, 1')
    p38 = Post(user_id=5, description='', createdAt='2021, 2, 1')
    p39 = Post(user_id=5, description='', createdAt='2021, 3, 1')
    p40 = Post(user_id=5, description='', createdAt='2021, 4, 1')
    p41 = Post(user_id=5, description='', createdAt='2021, 5, 1')
    
    p42 = Post(user_id=5, description='', createdAt='2021, 6, 1')
    
    p43 = Post(user_id=5, description='', createdAt='2021, 7, 1')
    p44 = Post(user_id=5, description='', createdAt='2021, 8, 1')
    p45 = Post(user_id=5, description='', createdAt='2021, 9, 1')
    
    p46 = Post(user_id=5, description='', createdAt='2021, 10, 1')
    
    p47 = Post(user_id=5, description='', createdAt='2021, 11, 1')
    p48 = Post(user_id=5, description='', createdAt='2021, 12, 1')



    p49 = Post(user_id=6, description='', createdAt='2021, 1, 1')
    p50 = Post(user_id=6, description='', createdAt='2021, 2, 1')
    p51 = Post(user_id=6, description='', createdAt='2021, 3, 1')
    p52 = Post(user_id=6, description='', createdAt='2021, 4, 1')
    p53 = Post(user_id=6, description='', createdAt='2021, 5, 1')
    p54 = Post(user_id=6, description='', createdAt='2021, 6, 1')
    p55 = Post(user_id=6, description='', createdAt='2021, 7, 1')
    p56 = Post(user_id=6, description='', createdAt='2021, 8, 1')
    p57 = Post(user_id=6, description='', createdAt='2021, 9, 1')
    p58 = Post(user_id=6, description='', createdAt='2021, 10, 1')
    p59 = Post(user_id=6, description='', createdAt='2021, 11, 1')
    p60 = Post(user_id=6, description='', createdAt='2021, 12, 1')



    p61 = Post(user_id=7, description='', createdAt='2021, 1, 1')
    p62 = Post(user_id=7, description='', createdAt='2021, 2, 1')
    p63 = Post(user_id=7, description='', createdAt='2021, 3, 1')
    p64 = Post(user_id=7, description='', createdAt='2021, 4, 1')
    
    p65 = Post(user_id=7, description='', createdAt='2021, 5, 1')
    
    p66 = Post(user_id=7, description='', createdAt='2021, 6, 1')
    p67 = Post(user_id=7, description='', createdAt='2021, 7, 1')
    p68 = Post(user_id=7, description='', createdAt='2021, 8, 1')
    p69 = Post(user_id=7, description='', createdAt='2021, 9, 1')
    p70 = Post(user_id=7, description='', createdAt='2021, 10, 1')
    p71 = Post(user_id=7, description='', createdAt='2021, 11, 1')
    p72 = Post(user_id=7, description='', createdAt='2021, 12, 1')



    p73 = Post(user_id=8, description='', createdAt='2021, 1, 1')
    p74 = Post(user_id=8, description='', createdAt='2021, 2, 1')
    p75 = Post(user_id=8, description='', createdAt='2021, 3, 1')
    p76 = Post(user_id=8, description='', createdAt='2021, 4, 1')
    
    p77 = Post(user_id=8, description='', createdAt='2021, 5, 1')
    
    p78 = Post(user_id=8, description='', createdAt='2021, 6, 1')
    p79 = Post(user_id=8, description='', createdAt='2021, 7, 1')
    p80 = Post(user_id=8, description='', createdAt='2021, 8, 1')
    
    p81 = Post(user_id=8, description='', createdAt='2021, 9, 1')
    
    p82 = Post(user_id=8, description='', createdAt='2021, 10, 1')
    p83 = Post(user_id=8, description='', createdAt='2021, 11, 1')
    p84 = Post(user_id=8, description='', createdAt='2021, 12, 1')



    p85 = Post(user_id=9, description='', createdAt='2021, 1, 1')
    p86 = Post(user_id=9, description='', createdAt='2021, 2, 1')
    p87 = Post(user_id=9, description='', createdAt='2021, 3, 1')
    p88 = Post(user_id=9, description='', createdAt='2021, 4, 1')
    p89 = Post(user_id=9, description='', createdAt='2021, 5, 1')

    p90 = Post(user_id=9, description='', createdAt='2021, 6, 1')
    p91 = Post(user_id=9, description='', createdAt='2021, 7, 1')

    p92 = Post(user_id=9, description='', createdAt='2021, 8, 1')
    p93 = Post(user_id=9, description='', createdAt='2021, 9, 1')
    p94 = Post(user_id=9, description='', createdAt='2021, 10, 1')
    p95 = Post(user_id=9, description='', createdAt='2021, 11, 1')
    p96 = Post(user_id=9, description='', createdAt='2021, 12, 1')



    p97 = Post(user_id=10, description='', createdAt='2021, 1, 1')
    p98 = Post(user_id=10, description='', createdAt='2021, 2, 1')
    p99 = Post(user_id=10, description='', createdAt='2021, 3, 1')
    p100 = Post(user_id=10, description='', createdAt='2021, 4, 1')
    p101 = Post(user_id=10, description='', createdAt='2021, 5, 1')
    p102 = Post(user_id=10, description='', createdAt='2021, 6, 1')
    p103 = Post(user_id=10, description='', createdAt='2021, 7, 1')
    p104 = Post(user_id=10, description='', createdAt='2021, 8, 1')
    p105 = Post(user_id=10, description='', createdAt='2021, 9, 1')
    p106 = Post(user_id=10, description='', createdAt='2021, 10, 1')
    p107 = Post(user_id=10, description='', createdAt='2021, 11, 1')
    p108 = Post(user_id=10, description='', createdAt='2022, 1, 1')



    p109 = Post(user_id=11, description='', createdAt='2021, 1, 1')
    p110 = Post(user_id=11, description='', createdAt='2021, 2, 1')
    p111 = Post(user_id=11, description='', createdAt='2021, 3, 1')
    p112 = Post(user_id=11, description='', createdAt='2021, 4, 1')
    p113 = Post(user_id=11, description='', createdAt='2021, 5, 1')
    p114 = Post(user_id=11, description='', createdAt='2021, 6, 1')
    p115 = Post(user_id=11, description='', createdAt='2021, 7, 1')
    p116 = Post(user_id=11, description='', createdAt='2021, 8, 1')
    p117 = Post(user_id=11, description='', createdAt='2021, 9, 1')
    p118 = Post(user_id=11, description='', createdAt='2021, 10, 1')
    p119 = Post(user_id=11, description='', createdAt='2021, 11, 1')
    p120 = Post(user_id=11, description='', createdAt='2021, 12, 1')


    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)
    db.session.add(p7)
    db.session.add(p8)
    db.session.add(p9)
    db.session.add(p10)
    db.session.add(p11)
    db.session.add(p12)
    db.session.add(p13)
    db.session.add(p14)
    db.session.add(p15)
    db.session.add(p16)
    db.session.add(p17)
    db.session.add(p18)
    db.session.add(p19)
    db.session.add(p20)
    db.session.add(p21)
    db.session.add(p22)
    db.session.add(p23)
    db.session.add(p24)
    db.session.add(p25)
    db.session.add(p26)
    db.session.add(p27)
    db.session.add(p28)
    db.session.add(p29)
    db.session.add(p30)
    db.session.add(p31)
    db.session.add(p32)
    db.session.add(p33)
    db.session.add(p34)
    db.session.add(p35)
    db.session.add(p36)
    db.session.add(p37)
    db.session.add(p38)
    db.session.add(p39)
    db.session.add(p40)
    db.session.add(p41)
    db.session.add(p42)
    db.session.add(p43)
    db.session.add(p44)
    db.session.add(p45)
    db.session.add(p46)
    db.session.add(p47)
    db.session.add(p48)
    db.session.add(p49)
    db.session.add(p50)
    db.session.add(p51)
    db.session.add(p52)
    db.session.add(p53)
    db.session.add(p54)
    db.session.add(p55)
    db.session.add(p56)
    db.session.add(p57)
    db.session.add(p58)
    db.session.add(p59)
    db.session.add(p60)
    db.session.add(p61)
    db.session.add(p62)
    db.session.add(p63)
    db.session.add(p64)
    db.session.add(p65)
    db.session.add(p66)
    db.session.add(p67)
    db.session.add(p68)
    db.session.add(p69)
    db.session.add(p70)
    db.session.add(p71)
    db.session.add(p72)
    db.session.add(p73)
    db.session.add(p74)
    db.session.add(p75)
    db.session.add(p76)
    db.session.add(p77)
    db.session.add(p78)
    db.session.add(p79)
    db.session.add(p80)
    db.session.add(p81)
    db.session.add(p82)
    db.session.add(p83)
    db.session.add(p84)
    db.session.add(p85)
    db.session.add(p86)
    db.session.add(p87)
    db.session.add(p88)
    db.session.add(p89)
    db.session.add(p90)
    db.session.add(p91)
    db.session.add(p92)
    db.session.add(p93)
    db.session.add(p94)
    db.session.add(p95)
    db.session.add(p96)
    db.session.add(p97)
    db.session.add(p98)
    db.session.add(p99)
    db.session.add(p100)
    db.session.add(p101)
    db.session.add(p102)
    db.session.add(p103)
    db.session.add(p104)
    db.session.add(p105)
    db.session.add(p106)
    db.session.add(p107)
    db.session.add(p108)
    db.session.add(p109)
    db.session.add(p110)
    db.session.add(p111)
    db.session.add(p112)
    db.session.add(p113)
    db.session.add(p114)
    db.session.add(p115)
    db.session.add(p116)
    db.session.add(p117)
    db.session.add(p118)
    db.session.add(p119)
    db.session.add(p120)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()


