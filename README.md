# chAirBears2



## Demo

[![](http://img.youtube.com/vi/9oLPJQTAut4/0.jpg)](http://www.youtube.com/watch?v=9oLPJQTAut4 "v1")



[![](http://img.youtube.com/vi/ErShXPqbcbo/0.jpg)](http://www.youtube.com/watch?v=ErShXPqbcbo "v2")



## Our goal is to achieve the following:

• Notify available seats in the libraries in the real-time

• Recommend the best time to go to the library that you can grab your seat with the highest possibility

• Suggest the best library depending on your study habit, noise preference, and the number of people

• Displays the number of people in the libraries

• Tell you when the libraries are opened or closed

## How did we build?

We built chAirBears2 using ImageAI, YOLO, and Cisco WebEx. ImageAI and YOLO were for the object detection, and Cisco WebEx was used for ChatBot. We determined the available seats using our own heuristic function, JSONified and sent this information to our ChatBot so that users can retrieve the library information in the real-time. Our ChatBot is trained based on the keywords.

## What is our future plan?

• Take a lot of pictures in the libraries so that we can improve the performance of object detection model.

• Crop photo automation. Since we were not able to complete the crop automation (for the better precision), we could not achieve decent precision with different images of libraries. Therefore, we cropped images manually to improve the detection performance, which is highly inefficient. We will automate this process so that we can guarantee the highest precision regardless of image quality.

• Live streaming of JSON data from the backend side to WebEx Chatbot so that we don’t have to manually upload the JSON files.

• Build a robust statistical-based model that includes: noise level, number of students depending on time and libraries, and so on.

• Using this statistical model, we can expect:

```
• the best and worst time to go to the library

• library recommendation module depending on the students' preference
```

• Train chatbot so that it can handle any questions. For example,

```
• 'How do I book the study room?`

• 'How do I get the locker?'

• 'Is library crowded now?'

• 'I have a group of three. Are there any seats where we all can have a seat together?'
```

There are still lots of things to work on.