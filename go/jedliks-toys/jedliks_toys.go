package jedlik

import "fmt"

// Drive updates the number of meters driven based on the car's speed,
// and reduces the battery according to the battery drainage.
func (c *Car) Drive() {
	if c.battery-c.batteryDrain >= 0 {
		c.distance += c.speed
		c.battery -= c.batteryDrain
	}
}

// DisplayDistance returns the distance as displayed on the LED display.
func (c Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %d meters", c.distance)
}

// DisplayBattery returns the battery percentage as displayed on the LED display.
func (c Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %d%%", c.battery)
}

// CanFinish returns true if the car can finish the race; otherwise, return false.
func (c Car) CanFinish(trackDistance int) bool {
	return (c.battery / c.batteryDrain * c.speed) >= trackDistance
}
