Set-Location $PSScriptRoot

Write-Host "=== Git status before ===" -ForegroundColor Cyan
git status

Write-Host "`n=== Adding files ===" -ForegroundColor Cyan
git add .

Write-Host "`n=== Creating commit ===" -ForegroundColor Cyan
git commit -m "Initial commit: contract management system"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Commit failed. Check git user.name and user.email." -ForegroundColor Red
    exit 1
}

Write-Host "`n=== Setting branch to main ===" -ForegroundColor Cyan
git branch -M main

Write-Host "`n=== Configuring remote ===" -ForegroundColor Cyan
git remote remove origin 2>$null
git remote add origin https://github.com/SkrinLeo/contract_system.git

Write-Host "`n=== Pushing to GitHub ===" -ForegroundColor Cyan
git push -u origin main

Write-Host "`nDone!" -ForegroundColor Green
