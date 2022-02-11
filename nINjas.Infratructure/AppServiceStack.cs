// Copyright 2016-2021, Pulumi Corporation.  All rights reserved.

using Pulumi;
using Pulumi.AzureNative.Insights;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Sql;
using Pulumi.AzureNative.Storage;
using Pulumi.AzureNative.Storage.Inputs;
using Pulumi.AzureNative.Web;
using Pulumi.AzureNative.Web.Inputs;

class AppServiceStack : Stack
{
    public AppServiceStack()
    {
        var resourceGroup = new ResourceGroup("appservice-rg", new ResourceGroupArgs { Location = "westeurope", ResourceGroupName = "appservice-rg" });

        var appServicePlan = new AppServicePlan("asp", new AppServicePlanArgs
        {
            ResourceGroupName = resourceGroup.Name,
            Kind = "App",
            Sku = new SkuDescriptionArgs
            {
                Tier = "Basic",
                Name = "B1",
            },
        });

        var app = new WebApp("app", new WebAppArgs { ResourceGroupName = "appservice-rg", Location = "westeurope", Name = "nINjas"});
    }
}
