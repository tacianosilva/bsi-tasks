#!/bin/bash

# Lista de repositórios e seus URLs
declare -A repos=(
    ["adm-bd"]="https://github.com/jtauanpm/adm-bd"
    ["adm-bd-dynamodb"]="https://github.com/jtauanpm/adm-bd-dynamodb"
    ["arq-comp-mips"]="https://github.com/jtauanpm/arq-comp-mips"
    ["calculo-limite"]="https://github.com/jtauanpm/calculo-limite"
    ["eng-soft-2"]="https://github.com/jtauanpm/eng-soft-2"
    ["origin"]="https://github.com/jtauanpm/origin"
    ["poo1"]="https://github.com/jtauanpm/poo1"
    ["poo2-flutter"]="https://github.com/jtauanpm/poo2-flutter"
    ["prog1-sig-finance"]="https://github.com/jtauanpm/prog1-sig-finance"
    ["pweb-react-lol"]="https://github.com/jtauanpm/pweb-react-lol"
    ["pweb-tasks"]="https://github.com/jtauanpm/pweb-tasks"
    ["redes-sdtp"]="https://github.com/jtauanpm/redes-sdtp"
    ["tcc"]="https://github.com/jtauanpm/tcc"
)

# Diretório onde os repositórios serão clonados
base_dir="bsi_tasks"

# Cria o diretório base se não existir
if [ ! -d "$base_dir" ]; then
    mkdir "$base_dir"
fi

# Função para clonar um repositório
clone_repo() {
    local name=$1
    local url=$2
    local repo_path="$base_dir/$name"
    
    if [ ! -d "$repo_path" ]; then
        echo "Cloning $name..."
        git clone "$url" "$repo_path"
        echo "$name cloned successfully."
    else
        echo "$name already exists, skipping."
    fi
}

# Clona todos os repositórios
for name in "${!repos[@]}"; do
    clone_repo "$name" "${repos[$name]}"
done

echo "All repositories have been cloned."
