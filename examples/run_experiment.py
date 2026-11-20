"""提案手法を評価するための実験プログラム（雛形）。"""

import csv
import sys
from pathlib import Path


def load_values(path: Path) -> list[float]:
    """CSVファイルの1列目を数値のリストとして読み込む。

    Args:
        path: 読み込むCSVファイルのパス。

    Returns:
        1列目の値を float に変換したリスト。

    Raises:
        FileNotFoundError: ファイルが存在しないとき。
        ValueError: 数値に変換できない値が含まれるとき。
    """
    with path.open(newline="", encoding="utf-8") as f:
        return [float(row[0]) for row in csv.reader(f) if row]


def average(values: list[float]) -> float:
    """数値のリストの平均を返す。

    Args:
        values: 平均を取る数値のリスト。

    Returns:
        平均値。

    Raises:
        ValueError: リストが空のとき。
    """
    if not values:
        raise ValueError("空のリストの平均は計算できません")
    return sum(values) / len(values)


def main() -> None:
    """コマンドライン引数で受け取ったCSVを読み込み、平均を表示する。"""
    if len(sys.argv) != 2:
        sys.exit("使い方: python run_experiment.py <データのCSV>")
    values = load_values(Path(sys.argv[1]))
    print(f"平均: {average(values)}")


if __name__ == "__main__":
    main()
