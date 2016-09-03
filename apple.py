width=input('please enter width:')
price_width=10
item_width=width-price_width
header_format='%-*s%*s'
format='%-*s%*.2f'
print"header_format%(item_width,'item',price_width,'price')'
print"'-'*width"
print'format%(item_width,'apples',price_width,0.4)'
