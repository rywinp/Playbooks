# Summary

## Video Demo
![DEMO VIDEO](https://www.youtube.com/watch?v=Pa-fxlMGKT8)

### Inspiration
We recognize the challenges teams face when striving for improvement together.
Analyzing footage recorded individually can often feel daunting, which is why 
we've developed a solution to transform this raw footage into a practical resource.

### What it does
Users can create an account to access a feature that converts their videos into an 
interactive clipboard software. This tool enables users to visually illustrate plays 
and strategies, simplifying the review process of on-field movements and facilitating
necessary adjustments for improvement. With the ability to draw on any frame and
save the annotated clipboard, users can thoroughly analyze what went wrong and
enhance their game.

### How we built it
With our deployed web application, which utilizes HTML for the frontend and Python with
Django for the backend, we have created a robust full-stack solution for users. By 
leveraging the Roboflow API to annotate our dataset and training our AI models for 
object detection using YOLOv8, we can analyze any recorded basketball play and infer player 
movements. With the capability to detect each player on the screen, this data is transformed 
into a 3D annotated clipboard, all made possible by our sophisticated design architecture.

### Challenges we ran into
We had trouble figuring out how to use roboflow models but once we understood, we were easily 
able to annotate our video with boxes that we could further feed to the user so that they 
could draw over it. We also struggled with our initial ideation. We also transitioned our 
code from colab to VSCode so that we could run it through the intel computer. We initially 
struggled with understanding how to connect and how to run it.

### Accomplishments that we are proud of
We learned how to use the Django framework and tailwind css. Addtionally, none of us had 
computer vision experience so this we learned how to use cv libraries and use other 
workflows like roboflow to speed up our application. We used the intel computer to speed 
up our application's speed by leveraging its compute power.

### What we learned
We learned Tailwind css, Django, computer vision, and how to use a gpu (namely the intel gpu).

### What's next for Playbook
Next up is the option for the user to receive a 2d image to draw over instead. We will 
also train a model to detect common basketball plays. From this, the user can easily detect 
what plays are being run in game footage and even obtain stats about their frequency and 
success rate.