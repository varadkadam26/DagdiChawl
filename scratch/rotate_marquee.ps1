Add-Type -AssemblyName System.Drawing

$files = @(
    "public/images/marquee/new_4.jpg",
    "public/images/marquee/new_9.jpg"
)

foreach ($f in $files) {
    $fullPath = (Resolve-Path $f).Path
    $bytes = [System.IO.File]::ReadAllBytes($fullPath)
    $ms = New-Object System.IO.MemoryStream($bytes, 0, $bytes.Length)
    $img = [System.Drawing.Image]::FromStream($ms)
    $img.RotateFlip([System.Drawing.RotateFlipType]::Rotate270FlipNone)
    
    $tmpPath = $fullPath + ".rotated.jpg"
    $img.Save($tmpPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $img.Dispose()
    $ms.Dispose()
    
    Move-Item -Force $tmpPath $fullPath
    Write-Host "Rotated 90 degrees left: $f"
}
