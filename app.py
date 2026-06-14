from flask import Flask, request

app = Flask(__name__)

birthday_message = """
Happy Birthday Yana! ❤️

I hope your day is filled with happiness,
laughter, blessings, and lots of love.

May all your dreams come true and may this year
bring you more success, good health, and unforgettable memories.

Enjoy your special day because you deserve all the happiness in the world.

Happy Birthday once again! 🎂🎉💖
"""

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Happy Birthday Yana</title>

        <style>
            body{
                margin:0;
                overflow:hidden;
                height:100vh;
                background:linear-gradient(135deg,#ffb6c1,#ff69b4,#ffc0cb);
                font-family:Arial,sans-serif;
                text-align:center;
                color:white;
            }

            h1{
                margin-top:150px;
                font-size:60px;
            }

            p{
                font-size:25px;
            }

            button{
                padding:12px 30px;
                font-size:20px;
                border:none;
                border-radius:25px;
                cursor:pointer;
            }

            .yes{
                background:white;
                color:#ff1493;
            }

            #noBtn{
                background:white;
                color:#ff1493;
                position:absolute;
            }

            .balloon{
                position:absolute;
                font-size:50px;
                animation:float 8s linear infinite;
            }

            @keyframes float{
                from{transform:translateY(100vh);}
                to{transform:translateY(-150px);}
            }
        </style>
    </head>

    <body>

        <div class="balloon" style="left:10%">🎈</div>
        <div class="balloon" style="left:30%;animation-delay:2s;">🎈</div>
        <div class="balloon" style="left:50%;animation-delay:4s;">🎈</div>
        <div class="balloon" style="left:70%;animation-delay:1s;">🎈</div>
        <div class="balloon" style="left:90%;animation-delay:3s;">🎈</div>

        <h1>Today's your birthday right? 💖</h1>

        <a href="/yes">
            <button class="yes">YES 💕</button>
        </a>

        <button id="noBtn">NO 😢</button>

        <script>
        const noBtn = document.getElementById("noBtn");

        function moveButton() {
            const maxX = window.innerWidth - noBtn.offsetWidth;
            const maxY = window.innerHeight - noBtn.offsetHeight;

            const randomX = Math.floor(Math.random() * maxX);
            const randomY = Math.floor(Math.random() * maxY);

            noBtn.style.left = randomX + "px";
            noBtn.style.top = randomY + "px";
        }

        noBtn.addEventListener("mouseenter", moveButton);
        noBtn.addEventListener("click", moveButton);

        moveButton();
        </script>

    </body>
    </html>
    """

@app.route("/yes")
def yes():
    return """
    <html>
    <body style="
        background:pink;
        color:white;
        text-align:center;
        font-family:Arial;
        padding-top:150px;
    ">
        <h1>🎂 Happy Birthday Yana!</h1>
        <h1>🎉 How old are you now? 🎉</h1>

        <form action="/age" method="post">
            <input type="number" name="age" required
            style="padding:10px;font-size:20px;">
            <br><br>

            <button type="submit"
            style="padding:10px 20px;font-size:18px;">
                Submit
            </button>
        </form>

    </body>
    </html>
    """

@app.route("/age", methods=["POST"])
def age():
    age = request.form["age"]

    return f"""
    <html>
    <body style="
        background:#ffb6c1;
        color:white;
        text-align:center;
        font-family:Arial;
        padding-top:150px;
    ">

        <h1>🎂 HAPPY BIRTHDAY! 🎂</h1>

        <h2>You are now {age} years old! 🎉</h2>

        <br>

        <a href="/message">
            <button style="
                padding:12px 25px;
                font-size:20px;
            ">
                Next ➜
            </button>
        </a>

    </body>
    </html>
    """

@app.route("/message")
def message():
    return f"""
    <html>
    <body style="
        background:#ff69b4;
        color:white;
        text-align:center;
        font-family:Arial;
        padding:40px;
    ">

        <h1>💖 A Special Message For You 💖</h1>

        <div style="
            max-width:800px;
            margin:auto;
            background:rgba(255,255,255,0.15);
            padding:25px;
            border-radius:20px;
        ">
            <p style="
                font-size:22px;
                line-height:1.8;
                white-space:pre-line;
            ">
                {birthday_message}
            </p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)




# import tkinter as tk
# import random

# def move_no_button():
#     # Random position sa "No" button
#     x = random.randint(0, 300)
#     y = random.randint(0, 200)
#     no_button.place(x=x, y=y)

# def first_yes():
#     output_label.config(text="Divah gwapo ko btw thank you yana!!")
#     next_button.pack()

# def next_question():
#     question_label.config(text="Proceed to the next question?")
#     output_label.config(text="")
#     next_button.pack_forget()

#     yes_button.config(command=second_question)
#     no_button.config(command=no_static)

# def no_static():
#     output_label.config(text="Okay, dili pa ta mo proceed.")

# def second_question():
#     question_label.config(text="Crush basadko nimo?")
#     output_label.config(text="")
#     yes_button.config(command=second_yes)
#     no_button.config(command=move_no_button)

# def second_yes():
#     output_label.config(text="Ikaw yana ha!! hilom hilom raka crush man sad diay ko nimo.")

# # Main window
# root = tk.Tk()
# root.title("Gwapo Ko Yana?")
# root.geometry("600x500")
# root.configure(bg="pink")  # pink background

# question_label = tk.Label(root, text="Gwapo ko yana?", font=("Arial", 35), bg="pink")
# question_label.pack(pady=20)

# yes_button = tk.Button(root, text="Yes", font=("Arial", 25), command=first_yes)
# yes_button.pack(side="left", padx=50)

# no_button = tk.Button(root, text="No", font=("Arial", 25))
# no_button.place(x=200, y=150)
# no_button.bind("<Enter>", lambda e: move_no_button())  # magbalhin kung i-hover

# output_label = tk.Label(root, text="", font=("Arial", 35), bg="pink")
# output_label.pack(pady=20)

# next_button = tk.Button(root, text="Next", font=("Arial", 35), command=next_question)

# root.mainloop()
