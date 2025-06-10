

#write a program to read the below dictionary and display the expected output

info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

for key,value in info.items():
    if type(value) is str:
        print(key.ljust(20),":", value)
        print("--------")
    if type(value) is dict:
        for skey,svalue in value.items():
            finalkey = key + " " + skey
            print(finalkey,":",svalue)
            