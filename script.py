# define ground shipping cost
def ground_shipping_cost(weight):
  if weight <= 2:
    cost = weight*1.50 + 20.00
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight*3.00 + 20.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight*4.00 + 20.00
    return cost
  else:
    cost = weight*4.75 + 20.00
    return cost

# define drone shipping cost
def drone_shipping_cost(weight):
  if weight <= 2:
    cost = weight*4.50
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight*9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight*12.00
    return cost
  else:
    cost = weight*14.25
    return cost

# define premium shipping cost
premium_shipping = 125

# calculate & compare the costs. print the cheapest method & price.
def compare_shipping(weight):
  if ground_shipping_cost(weight) < drone_shipping_cost(weight) and ground_shipping_cost(weight) < premium_shipping:
    return print("Ground shipping is the cheapest method." + str(ground_shipping_cost(weight)) + " dollars")
  elif drone_shipping_cost(weight) < ground_shipping_cost(weight) and drone_shipping_cost(weight) < premium_shipping:
    return print("Drone shipping is the cheapest method." + str(drone_shipping_cost(weight)) + " dollars")
  elif premium_shipping < drone_shipping_cost(weight) and premium_shipping < ground_shipping_cost(weight):
    return print("Premium shipping is the cheapest method." + "125" + " dollars")
  else:
    return print("All the shipping method is the same." + "125" + " dollars")





