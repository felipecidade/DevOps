function Generate-ComplexPassword {
    param (
        [int]$length = 20
    )

    $characters = @(
        [char[]]'ABCDEFGHIJKLMNOPQRSTUVWXYZ',      # Letras maiúsculas
        [char[]]'abcdefghijklmnopqrstuvwxyz',      # Letras minúsculas
        [char[]]'0123456789',                      # Números
        [char[]]'!@#$%^&*()_+-=[]{}|;:,.<>/?'      # Caracteres especiais
    )

    $password = ""

    # Garante que a senha tenha pelo menos um caractere de cada categoria
    foreach ($charSet in $characters) {
        $password += $charSet | Get-Random
    }

    # Preenche o restante da senha com caracteres aleatórios das categorias
    while ($password.Length -lt $length) {
        $randomCharSet = $characters | Get-Random
        $password += $randomCharSet | Get-Random
    }

    # Embaralha a senha para garantir que não haja uma ordem previsível
    $shuflePassword = ($password.ToCharArray() | Sort-Object {Get-Random})
    $password = -join $shuflePassword
    return $password
}

# Gerar uma senha com 16 caracteres
$generatedPassword = Generate-ComplexPassword -length 20
Write-Output "Generated Password: $generatedPassword"
