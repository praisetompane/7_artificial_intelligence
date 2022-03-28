from y_equal_x import straight_line
import matplotlib.pyplot as plt

# Starting with these "real world" events
price = [150000, 400000, 550000, 625000, 825000]
price_scale = 100000
price_scaled = [p/price_scale for p in price]

house_size = [1000, 2000, 3000, 4000, 5000]
house_size_scale = 1000
house_size_scaled = [hs/house_size_scale for hs in house_size]

plt.xlabel('house size in 1000 ft²')
plt.ylabel('House price in 100000s')
plt.scatter(house_size_scaled, price_scaled)


'''
    Guess a straight line to be the model
    m = 1 # slope of 1
'''
straight_line(plt, 1)

'''
    Guess a straight line to be the model
    m = 1.25 # slope of 1.25
'''
straight_line(plt, 1.25)

plt.show()

'''
    We(humans) can see/know that the m=1 line underestimates the values.
    ∴ We increase m
      BUT how would a computer know to INCREASE or DECREASE m?
        mₙₑw = mcᵤᵣᵣₑₙₜ - k  d
                          ----- E(m)
                           d(m)

            ENGLISH: current slope minus
                some constant k multiplied
                    by the derivative of the error function

                    i.e. error functionE(m) = maps slope to sum of errors squared = error value
                        i.e. error value = how wrong/incorrect is the line's predictions compared
                            to the actual real world values
'''

'''
references:
    Zach Star, The Mathematics of Machine Learning. https://www.youtube.com/watch?v=Rt6beTKDtqY'''
'''