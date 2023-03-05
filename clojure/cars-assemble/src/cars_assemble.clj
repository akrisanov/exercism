(ns cars-assemble)

(def cars-per-hour 221)

(defn production-rate
  "Returns the assembly line's production rate per hour,
   taking into account its success rate"
  [speed]
  (cond (<= speed 0) 0.0
        (<= speed 4) (* speed cars-per-hour 1.0)
        (<= speed 8) (* speed cars-per-hour 0.9)
        (<= speed 9) (* speed cars-per-hour 0.8)
        (<= speed 10) (* speed cars-per-hour 0.77)))

(defn working-items
  "Calculates how many working cars are produced per minute"
  [speed]
  (let [rate (production-rate speed)]
    (if (<= rate 0)
      0
      (int (/ rate 60)))))
