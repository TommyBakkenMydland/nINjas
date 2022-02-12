using Pulumi;
using System;
using System.Threading.Tasks;

namespace nINjas.Infratructure
{
    internal class Program
    {
        static void Main(string[] args)
        {
            static Task<int> Main() => Deployment.RunAsync<AppServiceStack>();
        }
    }
}
