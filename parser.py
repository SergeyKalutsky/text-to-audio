from itertools import chain

text = 'BTS (tiếng Hàn: 방탄소년단; Romaja: Bangtan Sonyeondan), còn được gọi là Bangtan Boys, là một nhóm nhạc nam Hàn Quốc được thành lập vào năm 2010 và ra mắt vào năm 2013 bởi Big Hit Entertainment.[5] Nhóm bao gồm 7 thành viên: Jin, Suga, J-Hope, RM, Jimin, V và Jungkook. Các thành viên đồng sáng tác và sản xuất phần lớn các sản phẩm âm nhạc của họ. Khởi đầu là một nhóm nhạc hip hop, phong cách âm nhạc của nhóm đã dần phát triển để thể hiện nhiều thể loại đa dạng. Ca từ của nhóm thường tập trung vào lời bình luận cá nhân và xã hội, đề cập đến các chủ đề về sức khỏe tinh thần, những rắc rối của tuổi học đường và tuổi thành niên, sự mất mát, hành trình hướng tới tình yêu bản thân và chủ nghĩa cá nhân. Các sản phẩm của nhóm còn thường đề cập đến khái niệm văn học, tâm lý học và bao gồm một cốt truyện vũ trụ song song.'
text = [val.split(',') for val in text.split('.')]
texts = [i.strip() for i in chain(*text) if i != '']
print(texts)