-- 코드를 입력하세요
SELECT
    board.TITLE, 
    board.BOARD_ID, 
    reply.REPLY_ID, 
    reply.WRITER_ID, 
    reply.CONTENTS, 
    DATE_FORMAT(reply.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD board
    JOIN USED_GOODS_REPLY reply
    ON board.BOARD_ID = reply.BOARD_ID
WHERE 1=1
    AND DATE_FORMAT(board.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY CREATED_DATE ASC, board.TITLE ASC