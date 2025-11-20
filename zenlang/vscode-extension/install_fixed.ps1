# Install ZenLang VS Code Extension
Write-Host "Installing ZenLang VS Code Extension..." -ForegroundColor Cyan

$extensionDir = "$env:USERPROFILE\.vscode\extensions\zenlang-1.0.0"
$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Create extension directory
Write-Host "Creating extension directory..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $extensionDir | Out-Null

# Copy extension files
Write-Host "Copying extension files..." -ForegroundColor Yellow
Copy-Item -Path "$sourceDir\*" -Destination $extensionDir -Recurse -Force

Write-Host ""
Write-Host "? ZenLang extension installed!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Restart VS Code" -ForegroundColor White
Write-Host "2. Open a .zen file" -ForegroundColor White
Write-Host "3. You should see:" -ForegroundColor White
Write-Host "   - ZenLang icon next to .zen files" -ForegroundColor Gray
Write-Host "   - Syntax highlighting" -ForegroundColor Gray
Write-Host "   - Auto-completion" -ForegroundColor Gray
Write-Host ""
Write-Host "Extension location: $extensionDir" -ForegroundColor Gray
