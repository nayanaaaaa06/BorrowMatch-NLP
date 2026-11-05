
import pandas as pd

data = [
    {
        "item_id": 1,
        "item_name": "Scientific Calculator",
        "category": "Electronics",
        "description": "Calculator for engineering mathematics and scientific calculations",
        "condition": "Good",
        "availability": "Available",
        "owner": "Rahul"
    },
    {
        "item_id": 2,
        "item_name": "Engineering Drawing Kit",
        "category": "Stationery",
        "description": "Drawing instruments including compass, divider and scale",
        "condition": "Excellent",
        "availability": "Available",
        "owner": "Priya"
    },
    {
        "item_id": 3,
        "item_name": "Laptop",
        "category": "Electronics",
        "description": "Laptop for programming, Python development and college projects",
        "condition": "Good",
        "availability": "Available",
        "owner": "Arjun"
    },
    {
        "item_id": 4,
        "item_name": "Python Programming Book",
        "category": "Books",
        "description": "Beginner friendly Python programming and coding textbook",
        "condition": "Good",
        "availability": "Available",
        "owner": "Sneha"
    },
    {
        "item_id": 5,
        "item_name": "DSA Textbook",
        "category": "Books",
        "description": "Data structures and algorithms textbook for computer science students",
        "condition": "Excellent",
        "availability": "Available",
        "owner": "Kiran"
    },
    {
        "item_id": 6,
        "item_name": "Headphones",
        "category": "Electronics",
        "description": "Wireless headphones for online classes and study sessions",
        "condition": "Good",
        "availability": "Available",
        "owner": "Megha"
    },
    {
        "item_id": 7,
        "item_name": "College Backpack",
        "category": "Accessories",
        "description": "Spacious backpack for carrying books, laptop and stationery",
        "condition": "Good",
        "availability": "Available",
        "owner": "Vikram"
    },
    {
        "item_id": 8,
        "item_name": "Arduino Uno Kit",
        "category": "Electronics",
        "description": "Microcontroller development kit for electronics and IoT projects",
        "condition": "Excellent",
        "availability": "Available",
        "owner": "Ananya"
    },
    {
        "item_id": 9,
        "item_name": "Machine Learning Book",
        "category": "Books",
        "description": "Introduction to machine learning, artificial intelligence and deep learning",
        "condition": "Good",
        "availability": "Available",
        "owner": "Rohit"
    },
    {
        "item_id": 10,
        "item_name": "USB Pendrive",
        "category": "Accessories",
        "description": "32GB USB storage device for transferring academic files and projects",
        "condition": "Good",
        "availability": "Available",
        "owner": "Divya"
    },
    {
        "item_id": 11,
        "item_name": "Webcam",
        "category": "Electronics",
        "description": "External webcam for video conferencing and online meetings",
        "condition": "Good",
        "availability": "Available",
        "owner": "Akhil"
    },
    {
        "item_id": 12,
        "item_name": "Operating Systems Book",
        "category": "Books",
        "description": "Textbook covering operating systems, processes and memory management",
        "condition": "Excellent",
        "availability": "Available",
        "owner": "Pooja"
    }
]

df = pd.DataFrame(data)

df.to_csv("borrow_items.csv", index=False)

print("Database generated successfully!")
print(f"Total items added: {len(df)}")
print("\nDataset preview:")
print(df.head())
