from pyscript import display, document

document.getElementById('sku_output').innerHTML = " "
category = document.getElementById('category').value
product_name = document.getElementById('product_name').value
stock_qty = document.getElementById('quantity').value

sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
display(f"SKU: {sku}", target='sku_output')
