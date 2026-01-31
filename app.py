from flask import Flask,render_template,request
from bot.orders import place_order

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    result=None
    error=None

    if request.method=="POST":
        try:
            symbol=request.form.get('symbol')
            side=request.form.get('side')
            order_type=request.form.get('order_type')
            quantity=request.form.get('quantity')
            price=request.form.get('price')or None
            result=place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )
        except Exception as e:
            error=str(e)

    return render_template('index.html',result=result,error=error)

if __name__=="__main__":
    app.run(debug=True)
