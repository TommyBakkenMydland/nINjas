using Pulumi;

static Task<int> Main() => Deployment.RunAsync<AppServiceStack>();