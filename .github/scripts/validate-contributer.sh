#!/usr/bin/env bash

function contains() {
  local n=$#
  local value=${!n}
  for ((i = 1; i < $#; i++)); do
    if [ "${!i}" == "${value}" ]; then
      echo "y"
      return 0
    fi
  done
  echo "n"
  return 1
}

assert_names() {
  dir_repo="$(pwd ../../)"
  dir_hw="${dir_repo}/hw"
  dir_names=$(ls -d ${dir_hw}/* | sed -e 's/.*hw\///g')
  github_names=(
    "alexander_sidorov"
    "alexey_tyuhai"
    "andrey_karpuk"
    "dmitry_mihayluk"
    "eugene_bakun"
    "eugene_ladyko"
    "eugene_lubimov"
    "eugene_vavilov"
    "igor_maximov"
    "maxim_baranov"
    "maxim_lomako"
    "nikita_karmanov"
    "sergey_sakovich"
    "vadim_zharski"
    "vladislav_yurenia"
    "yana_sergienko"
  )

  for n in ${dir_names}; do
    if [[ $n == "__init__.py" ]]; then
      continue
    fi

    if [[ $(contains "${github_names[@]}" "$n") == "n" ]]; then
      echo "unknown dir in hw/: '$n/'"
      return 1
    fi

    pkg_init_py="${dir_hw}/$n/__init__.py"
    if [[ ! -f $pkg_init_py ]]; then
      echo "File '__init__.py' MUST be added to '${dir_hw}/$n/'"
      return 1
    fi
  done
}

assert_names
