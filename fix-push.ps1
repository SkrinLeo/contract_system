Set-Location $PSScriptRoot

Write-Host "=== Pulling remote changes ===" -ForegroundColor Cyan
git pull origin main --allow-unrelated-histories --no-edit
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pull failed. If there is a merge conflict, open conflicted files, fix them, then run:" -ForegroundColor Red
    Write-Host "  git add ." -ForegroundColor Yellow
    Write-Host "  git commit -m 'Merge remote README'" -ForegroundColor Yellow
    Write-Host "  git push -u origin main" -ForegroundColor Yellow
    exit 1
}

Write-Host "`n=== Pushing to GitHub ===" -ForegroundColor Cyan
git push -u origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "Push failed." -ForegroundColor Red
    exit 1
}

Write-Host "`nSuccess! Repository is on GitHub." -ForegroundColor Green
