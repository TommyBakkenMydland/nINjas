using Microsoft.AspNetCore.Mvc;
using Microsoft.PowerPlatform.Dataverse.Client;
using Microsoft.Xrm.Sdk.Query;

namespace nINjas.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ShoppingListController : ControllerBase
    {
        private readonly ILogger<ShoppingListController> _logger;

        public ShoppingListController(ILogger<ShoppingListController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public async Task<IEnumerable<Shopping>> Get()
        {
            var clientId = "bbe29d95-52cf-4e49-9866-d2cfb3c78f5c";
            var clientSecret = @$"eN~7Q~LLouom4lAtZy2HrWsRjwu7kI~pcZFlO";
            var environment = "org49e96989";

            var connectionString = @$"Url=https://{environment}.crm4.dynamics.com;AuthType=ClientSecret;ClientId={clientId};ClientSecret={clientSecret};RequireNewInstance=true";
     
                using var serviceClient = new ServiceClient(connectionString);

                var shoppingCollection = await serviceClient. RetrieveMultipleAsync(new QueryExpression("ninjas_ingredient")
                {
                    ColumnSet = new ColumnSet("ninjas_name", "ninjas_infridge"),
                    TopCount = 10
                });

                var shoppingData = shoppingCollection.Entities
                    .Select(x => $"{x.GetAttributeValue<string>("ninjas_name")}, {x.GetAttributeValue<bool>("ninjas_infridge")}")
                    .ToList();

                var shoppingList = new List<Shopping>();

                foreach(var shopping in shoppingData)
                {
                    var test = shopping.Split(", ").First();
                    shoppingList.Add(new Shopping { Name = shopping.Split(", ").First(), InFridge = bool.Parse(shopping.Split(',').Last()) });
                }
                return shoppingList.Where(x => x.InFridge != true).ToArray();
    
     
         
            
        }
    }
}