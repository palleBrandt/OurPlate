using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using 

namespace OurPlate.Api.Controllers;

[ApiController]
[Route("[controller]")]
public class RecipeController : ControllerBase
{
    private readonly ILogger<RecipeController> _logger;

    public RecipeController(ILogger<RecipeController> logger)
    {
        _logger = logger;
    }

    [HttpGet("{recipes}")]
    public IEnumerable<Recipe> 

        
        
}

