import logging

logging.basicConfig(
    format="[%(asctime)-15s %(name)-5s %(levelname)s] %(message)s", level=logging.INFO
)

main_logger = logging.getLogger(__name__)
