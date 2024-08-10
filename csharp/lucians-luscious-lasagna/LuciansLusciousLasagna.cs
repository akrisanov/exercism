class Lasagna
{
    /// <summary>
    /// How many minutes the lasagna should be in the oven.
    /// </summary>
    public int ExpectedMinutesInOven() => 40;

    /// <summary>
    /// How many minutes the lasagna still has to remain in the oven.
    /// </summary>
    /// <param name="minutesInOven">The actual minutes the lasagna has been in the oven</param>
    public int RemainingMinutesInOven(int minutesInOven)
    {
        return ExpectedMinutesInOven() - minutesInOven;
    }

    /// <summary>
    /// How many minutes will be spent preparing the lasagna.
    /// </summary>
    /// <param name="layers">The number of layers to add to the lasagna</param>
    public int PreparationTimeInMinutes(int layers)
    {
        // each layer takes you 2 minutes to prepare:
        return layers * 2;
    }

    /// <summary>
    /// How many minutes you've worked on cooking the lasagna.
    /// </summary>
    /// <param name="layers">The number of layers added to the lasagna</param>
    /// <param name="minutesInOven">The number of minutes the lasagna has been in the oven</param>
    /// <returns></returns>
    public int ElapsedTimeInMinutes(int layers, int minutesInOven)
    {
        return PreparationTimeInMinutes(layers) + minutesInOven;
    }
}
