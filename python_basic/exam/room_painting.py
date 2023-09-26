import math

paint_boxes = int(input())
rolls_paper = int(input())
one_pair_gloves_price = float(input())
one_brush_price = float(input())

paint_boxes_price = paint_boxes * 21.50
rolls_papers_price = rolls_paper * 5.20
needed_gloves_price = math.ceil(rolls_paper * 0.35) * one_pair_gloves_price
brush_price = math.floor(paint_boxes * 0.48) * one_brush_price

total_price = paint_boxes_price + rolls_papers_price + needed_gloves_price + brush_price
final_price = total_price / 15
print(f"This delivery will cost {final_price :.2f} lv.")