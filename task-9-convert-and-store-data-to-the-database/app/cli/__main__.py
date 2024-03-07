import argparse

from app.config import settings
from app.logic.report.report import (
    Report, 
    validator_not_exist_files
)
from app.db.utils import (
    create_database, 
    drop_database, 
    init_db,
    load_data_to_db
)


def parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--files",
        dest='folder_path',
        help="Folder containing files",
        default="data"
    )
    parser.add_argument(
        "--load",
        action="store_true",
        help="Insert data into database",
    )
    parser.add_argument(
        "--init",
        action="store_true",
        help="Init DB",
    )
    parser.add_argument(
        "action",
        choices=["print","create", "init", "drop", "load"],
        help="Choice db action",
    )
    parser.add_argument(
        '--asc',
        dest='order_by',
        action='store_const',
        const='asc',
        help='Sort in ascending order (default)'
    )
    parser.add_argument(
        '--desc',
        dest='order_by',
        action='store_const',
        const='desc',
        help='Sort in descending order'
    )
    parser.add_argument(
        '--driver',
        dest='driver',
        help='Show statistics about a specific driver'
    )
    parser.add_argument(
        '--print',
        dest='print',
        help='Print report'
    )

    return parser.parse_args()

def main() -> None:
    args = parser()

    if args.action == "drop":
        drop_database(db_name=settings.DB_NAME)
        return

    if args.action == "create":
        create_database(db_name=settings.DB_NAME)

    if args.action == "recreate":
        drop_database(db_name=settings.DB_NAME)
        create_database(db_name=settings.DB_NAME)

    if args.action == "init" or args.init:
        init_db(db_name=settings.DB_NAME, db_url=settings.DATABASE_URL_psycopg)

    if args.action in ["load", "print"]:
        if not_files := validator_not_exist_files(args.folder_path):
            raise FileNotFoundError(
                f"For folder path {args.folder_path} files not found: "
                f"{', '.join(not_files)}"
            )
        
        report_instance = Report(
            folder_path=args.folder_path,
            order_by=args.order_by,
            driver=args.driver
        )

        if args.action == "load":
            load_data_to_db(report_instance, args.folder_path)

        if args.action == "print":
            report_instance.print_report()


if __name__ == '__main__':
    main()
