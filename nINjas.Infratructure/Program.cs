
using Pulumi;
class program
{
    static Task<int> Main() => Deployment.RunAsync<AppServiceStack>();
}

