import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Trợ lý Giáo dục 7991", layout="wide")
st.title("🎯 TRỢ LÝ AI SOẠN ĐỀ KIỂM TRA ĐỊNH KỲ (CHUẨN CV 7991)")
st.caption("Ứng dụng tự động xây dựng Ma trận - Bản đặc tả - Đề thi & Đáp án chuẩn Bộ GD&ĐT")

# Tự động lấy mã API Key an toàn từ mục Secrets của Streamlit
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key="AQ.AbBRN6LcDMmGVvu51zn9MXuKo6y4gpN128XrNBOcaB6ybNz-rw")    
    # Sử dụng bộ não dự phòng thông minh để chống lỗi NotFound
    model_names = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-1.5-pro']

    col1, col2 = st.columns(2)
    with col1:
        mon_hoc = st.text_input("Môn học:", placeholder="Ví dụ: Công nghệ, Ngữ văn...")
        khoi_lop = st.selectbox("Khối lớp:", ["Khối 6", "Khối 7", "Khối 8", "Khối 9", "Khối 10", "Khối 11", "Khối 12"])
    with col2:
        hinh_thuc = st.selectbox("Hình thức kiểm tra:", ["Giữa học kỳ 1", "Cuối học kỳ 1", "Giữa học kỳ 2", "Cuối học kỳ 2"])
        pham_vi = st.text_area("Phạm vi kiến thức:", placeholder="Ví dụ: Bài 1, Bài 2, Bài 3...")

    if st.button("🚀 BẮT ĐẦU KHỞI TẠO ĐỀ THI"):
        with st.spinner("AI đang thiết lập theo Công văn 7991... Vui lòng đợi trong giây lát!"):
            prompt = f"Biên soạn bộ tài liệu kiểm tra cho môn {mon_hoc}, lớp {khoi_lop}, kỳ thi {hinh_thuc} thuộc phạm vi kiến thức: {pham_vi}. Yêu cầu tuân thủ nghiêm ngặt tinh thần Công văn 7991/BGDĐT-GDTrH: 1. Tạo Khung ma trận đề kiểm tra (định dạng bảng rõ ràng, phân chia theo 4 mức độ: Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao; tỷ lệ điểm kiểm tra là 70% Trắc nghiệm và 30% Tự luận). 2. Bản đặc tả đề kiểm tra. 3. Đề kiểm tra chi tiết. 4. Đáp án và hướng dẫn chấm chi tiết."
            
            success = False
            for name in model_names:
                try:
                    active_model = genai.GenerativeModel(name)
                    response = active_model.generate_content(prompt)
                    st.success(f"🎉 Đã khởi tạo đề thi thành công!")
                    st.markdown(response.text)
                    success = True
                    break
                except Exception as e:
                    continue
            
            if not success:
                st.error("Lỗi xác thực: Mã khóa API Key trong mục Secrets của Streamlit bị sai ký tự. Thầy/cô vui lòng kiểm tra lại mã ở tab Google AI Studio.")
else:
    st.error("Chưa cấu hình API Key trong mục Secrets của Streamlit.")
