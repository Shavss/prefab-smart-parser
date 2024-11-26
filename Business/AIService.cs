using Core.Enums;

namespace Business;

public class AIService : IAIService
{
    public async Task<string> ReadStructuredData(string filePath, LlmEnum llm)
    {
        if (llm != LlmEnum.OpenAi)
        {
            throw new ArgumentOutOfRangeException(nameof(llm), "selected llm is not supported");
        }

        const string baseUrl = "http://127.0.0.1:5000/api/parseit";
        const string parameterName = "input";
        var apiUrl = $"{baseUrl}?{parameterName}={filePath}";
        using var client = new HttpClient();
        var response = await client.GetAsync(apiUrl);
        response.EnsureSuccessStatusCode();
        var responseData = await response.Content.ReadAsStringAsync();
        return responseData;
    }
}