# when you open cli/ cmd the first thing it will show is default location. 
        # is the set of location is called path?

        # No, a set of locations is not necessarily called a path.

        # A path typically refers to a sequence of locations that are connected in some way, such as a path through a forest or a path along a street. A path may be defined by a specific starting and ending location, or it may be an open-ended route that can be extended or modified.

        # A set of locations, on the other hand, is simply a collection of individual points or places, and may or may not be connected in any meaningful way.




        # how a path is represented explain with some examples 

        # A path can be represented in different ways depending on the context and the purpose. Here are some common ways that paths can be represented:

        # Textual representation: A path can be represented as a sequence of locations or landmarks written in text, such as "Start at the park entrance, turn right at the first intersection, and continue straight until you reach the museum." This type of representation is often used for giving directions or instructions.

        # Graph representation: A path can be represented as a sequence of vertices (nodes) and edges in a graph, where each vertex represents a location and each edge represents a connection between two locations. For example, a path from a starting location A to an ending location D might be represented as the sequence of vertices {A, B, C, D} and edges {(A,B), (B,C), (C,D)}. This type of representation is often used in computer science and mathematics.

        # Map representation: A path can be represented visually on a map, where each location is marked as a point and the path is shown as a line connecting the points. This type of representation is often used for navigation and tourism purposes.

        # Spatial database representation: A path can be represented as a series of geographic coordinates in a spatial database, such as latitude and longitude or UTM (Universal Transverse Mercator) coordinates. This type of representation is often used in GIS (Geographic Information Systems





        # give me an example of how a path look like 

        # Sure! Here's an example of how a path might look like:

        # Imagine that you are walking from your home to a nearby park. The path you take might look something like this:

        # Start at your home on Main Street
        # Turn right onto First Avenue
        # Continue straight on First Avenue for two blocks
        # Turn left onto Elm Street
        # Cross the bridge over the creek
        # Turn right onto Maple Street
        # Continue straight on Maple Street for three blocks
        # Turn left onto Oak Avenue
        # Walk two more blocks until you reach the park entrance on your left.
        # This is an example of a path represented in a textual format, with a sequence of locations and directions to follow. It can also be represented on a map as a line connecting the points where you turn or continue straight, giving a visual representation of the path you take.
# so that's mean --> C:\Users\rekha>   <-- this is the location of my terminal .
# but the main thing you should be aware of that this is my assigned location that means i have setted this location. 
# so if we want to find out our previous location / means default location then we will follow the following steps -- 
#  first of all we need to think bout what exactly we are trying to do ?
# we are already in a location and we want to switch that with the previous location / we want to go back to our previous location 
# for that type --> cd /--> now what does this do ? cd stands for 'change directory' so we are telling cmd to change the directory 
# and bcz we dont want to open any folder that's why  the '/' is here-->
# in cmd we will see -- > C:\>----> that means we are not in any folder ---> 
# again we will type --> cd users ---> the command is saying change the directory/location  to the users folder --->
    # is directory refers to the location in the computer science 
    # Yes, in computer science, a directory typically refers to a location in a file system where files and subdirectories can be stored. A directory can also be referred to as a folder. Directories are used to organize files and make it easier to locate and access them.
    # Directories are typically arranged in a hierarchical tree structure, with the top-level directory (also known as the root directory) at the top, and subdirectories branching out from there. Each directory can contain files and other subdirectories, which can also have their own subdirectories and files.
    # In command-line interfaces and operating systems, directories are represented by a path, which specifies the sequence of directories that must be navigated in order to reach a specific file or directory. For example, the path "/home/user/documents" would refer to the "documents" directory located within the "user" directory, which in turn is located within the "home" directory.
# and we will get inside of the users folder -->and then we want to go to our named folder -->
# so we will type --> cd rekha  ---> with this we are move to the rekha folder 
# now upto this we can certainly make some observation such as --  
# each time we move to a certain location it 's gonna add to the path . 
# before move to any location we have to mind that its gonna move from current location/directory  .
 
 
 
 
 
 
 
# # code untill now 
# Microsoft Windows [Version 10.0.22623.1028]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\rekha>cd/

# C:\>c users
# 'c' is not recognized as an internal or external command,
# operable program or batch file.

# C:\>cd users

# C:\Users>cd rekha

# C:\Users\rekha>