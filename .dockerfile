# Usar la imagen base de .NET
FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["FerreteriaBackend/FerreteriaBackend.csproj", "FerreteriaBackend/"]
RUN dotnet restore "FerreteriaBackend/FerreteriaBackend.csproj"
COPY . .
WORKDIR "/src/FerreteriaBackend"
RUN dotnet build "FerreteriaBackend.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "FerreteriaBackend.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FerreteriaBackend.dll"]
