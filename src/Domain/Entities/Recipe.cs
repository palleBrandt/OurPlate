
namespace OurPlate.Domain;

public class Recipe
{
    public string Id { get; set; }
    public required string Name { get; set; }
    public List<Ingredient> Ingredients { get; set; } = new List<Ingredient>();
}

