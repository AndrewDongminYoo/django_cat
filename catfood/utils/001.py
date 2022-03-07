from first import Crawler, Brand

if __name__ == '__main__':
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Natural Balance")[0],
        analysis="#tab-nutrition > div > div.left > div > div",
        ingredients="#tab-nutrition > div > div.right > div > div:nth-child(1) > div",
        calorie="#tab-nutrition > div > div.right > div > div:nth-child(2) > div"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Hill's Science Diet")[0],
        analysis="#content > div > div > div > div > div.accordion.component.section.accordion-product-detail.odd.col-xs-12.initialized > div > ul > li.accordion-slide.last > div > div > div > div.box.component.section.box-product-detail.first.odd.col-xs-12 > div > div > div.productAwareRichText.richText.component.section.default-style.odd.col-xs-12.initialized > div > div > div > table > tbody",
        ingredients="div.component-content > div > div.productAwareRichText.richText.component.section.default-style.even.col-xs-12.col-sm-8.initialized > div > div > p",
        calorie="div.productAwareRichText.richText.component.section.default-style.even.col-xs-12 h6"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Wellness")[0],
        ingredients="#block-wellness-content > div > section.section-padding.product-detail-wysiwyg > div > div.product-detail-wysiwyg-block.ingredients > p:nth-child(2)",
        analysis="#tableWrapperWrapper > div.table-container > table > tbody",
        calorie="#tableWrapperWrapper > div.table-container > table > tbody > tr > td:-soup-contains(kcal)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Alpha Spirit")[0],
        ingredients="#AddToCartForm--product-template > div.product-description.rte > div:nth-child(3) > div > p:nth-child(3) > span",
        analysis="#AddToCartForm--product-template > div.product-description.rte > div:nth-child(3) > div > table > tbody",
        additives="#AddToCartForm--product-template > div.product-description.rte > div:nth-child(3) > div > p:nth-child(4) > span"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Nutro Natural Choice")[0],
        analysis="#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(1) > div > div > dl:nth-child(2) > dd > div > table > tbody",
        ingredients="#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(2) > div > ul",
        calorie="#product > section:nth-child(5) > div > div > div.two-third.break-half > section:nth-child(1) > div > div:nth-child(1) > div > div > dl:nth-child(2) > dd > div > table > tbody > tr:last-child > td:nth-child(2)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Nutro Natural Choice")[0],
        analysis="body > main > section.proDetSec2 > div > div > div:nth-child(2) > div > table > tbody",
        ingredients="body > main > section.proDetSec2 > div > div > div:nth-child(1) > div > p",
        calorie="body > main > section.proDetSec3 > div > div > div:nth-child(2) > div > p:-soup-contains(calculated)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Natural Greatness")[0],
        ingredients="div.elementor-text-editor.elementor-clearfix > :-soup-contains(Mineral)",
        analysis="div.elementor-text-editor.elementor-clearfix > :-soup-contains(Crude)",
        calorie="div.elementor-text-editor.elementor-clearfix > div > :-soup-contains(kcal)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Sanabelle")[0],
        ingredients="#zusammensetzung > div > p:nth-child(3)",
        analysis="#analyt > div > div > div.modal-body",
        additives="#zusatzstoffe > div > div > div.modal-body > p"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Whiskas")[0],
        ingredients="body > main > div:nth-child(1) > section.pdSec2 > div > div.col-xs-12.col-sm-6.xs-m-b-15 > div > p",
        analysis="body > main > div:nth-child(1) > section.pdSec3 > div > div:nth-child(2) > div > table > tbody",
        calorie="body > main > div:nth-child(1) > section.pdSec3 > div > div:nth-child(2) > div.color-cont > div"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Instinct Pet Food")[0],
        ingredients="#our-ingredients > div > p",
        analysis="#nutritional-info > div > div:nth-child(4)",
        calorie="#nutritional-info > div > div:nth-child(3) > div > div > div:nth-child(2) > div"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Nutrience")[0],
        ingredients="body > div.main-container > div.container.product-info-ctn > div:nth-child(3) > div.col-md-7.offset-lg-1 > div.features-details-ctn > div.product-details-ctn > div:nth-child(1) > div",
        analysis="#tabs-3 > #analysis-table > tbody",
        calorie="#tabs-3 > p:-soup-contains(kcal)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Nutram Canada")[0],
        ingredients="",
        analysis="",
        calorie=""
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Against The Grain")[0],
        ingredients="div.entry.page.type-page.status-publish.entry div.entry_post > p:-soup-contains(Vitamins)",
        analysis="#content > div.sidebar_down > div:nth-child(1) > div.container_widgets_pieces > div.widget_center.widget_content > div > table > tbody",
        calorie="#content > div.sidebar_down > div:nth-child(1) > div.container_widgets_pieces > div.widget_center.widget_content > div > table > tbody > tr:last-child"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Cardinal Fussie Cat")[0],
        ingredients="div > div.elementor-element.elementor-widget.elementor-widget-heading > div > div.elementor-heading-title.elementor-size-default",
        analysis="div.elementor-element.elementor-widget.elementor-widget-heading > div > div:-soup-contains(Crude)",
        calorie="div.elementor-container.elementor-column-gap-default div.elementor-row div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element:nth-child(1) div.elementor-column-wrap.elementor-element-populated div.elementor-widget-wrap div.elementor-element.elementor-widget.elementor-widget-heading > div.elementor-widget-container"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Forza10 USA")[0],
        ingredients="#tab__Nutritional-Info > div > p:nth-child(2)",
        analysis="#tab__Nutritional-Info > div > p:nth-child(4)",
        calorie="#tab__Nutritional-Info > div > p:nth-child(3)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="KOOKUT")[0],
        ingredients="section > div > div.product__info-wrapper.grid__item > div > div:nth-child(12) > details > div > p > span",
        analysis="section > div > div.product__info-wrapper.grid__item > div > div:nth-child(13) > details > div > p > span"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="MeowMix")[0],
        ingredients="#tab-nutrition-collapse-0 > div > div.left > p",
        analysis="#tab-nutrition-collapse-0 > div > div.right > div.guaranteed-analysis > div"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="ZiwiPeak")[0],
        ingredients="#quickset-tabs_air_dried_and_canned_no_ta > div > div.view.view-pdp-2019-page-elements.resp-tab-content > div > div > div > div > div > div.pdp-ingredients-list",
        analysis="#quickset-tabs_air_dried_and_canned_no_ta > div > div.view.view-pdp-2019-page-elements.resp-tab-content > div.view-content > div",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Chicken Soup for the Soul")[0],
        ingredients="div.view-mode-full > div.field-wrapper.field.field-node--field-ingredients.field-name-field-ingredients.field-type-text-long.field-label-above > div > div > p:nth-child(2)",
        analysis="div.view-mode-full > div.field-wrapper.field.field-node--field-guaranteed-analysis.field-name-field-guaranteed-analysis.field-type-text-long.field-label-above > div > div > table > tbody",
        calorie="div.view-mode-full > div.field-wrapper.field.field-node--field-calorie-content.field-name-field-calorie-content.field-type-text-long.field-label-above > div > div > p:nth-child(2)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Merrick")[0],
        ingredients="#ingredients > p",
        analysis="#guaranteed-analysis > div > div.analysis__table.col-12.col-md-6",
        calorie="#feeding-guide > div.feeding-guide__wrapper > div.feeding-guide__additional > p:nth-child(4)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="NutriSource")[0],
        ingredients="#ingredients-nutrition > div.et_pb_row.et_pb_row_4 > div.et_pb_column.et_pb_column_2_3.et_pb_column_6.et_pb_css_mix_blend_mode_passthrough > div.et_pb_module.et_pb_text.et_pb_text_10.et_pb_text_align_left.et_pb_bg_layout_light > div > p:nth-child(2)",
        calorie="#ingredients-nutrition > div.et_pb_row.et_pb_row_4 > div.et_pb_column.et_pb_column_1_3.et_pb_column_7.et_pb_css_mix_blend_mode_passthrough.et-last-child > div > div > table > tbody",
        analysis="#ingredients-nutrition > div.et_pb_row.et_pb_row_4 > div.et_pb_column.et_pb_column_2_3.et_pb_column_6.et_pb_css_mix_blend_mode_passthrough > div.et_pb_module.et_pb_text.et_pb_text_11.et_pb_text_align_left.et_pb_bg_layout_light > div > table > tbody"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Thrive complete")[0],
        ingredients="#po2",
        analysis="#po3"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Weruva Catfood")[0],
        ingredients="#nutritionDetailInfo > div > div.col-md-8.col-xl-7.order-first > div.product-extra-detail.product-ingredients-detail > p:nth-child(3)",
        analysis="#nutritionDetailInfo > div > div.col-md-4 > div:nth-child(2) > table",
        calorie="#nutritionDetailInfo > div > div.col-md-4 > div:nth-child(1) > table > tbody"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Optimanova")[0],
        ingredients="#contenido-2 > div > div > div:nth-child(2) > div.col-xs-8.column > div.composicion.infosec > div.info",
        analysis="#contenido-2 > div > div > div:nth-child(2) > div.col-xs-8.column > div:nth-child(3) > div.info",
        additives="#contenido-2 > div > div > div:nth-child(2) > div.col-xs-8.column > div:nth-child(4) > div.info"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Organix")[0],
        ingredients="#ingredientsContentContainer > div > p:nth-child(1)",
        analysis="#analysisContentContainer > div > div > table",
        calorie="#feedingGuideContentContainer > div > div > label > p:last-child"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Rawz")[0],
        ingredients="#our-recipe > div:nth-child(2) > div.ingredients-column > div",
        analysis="#guaranteed-analysis > div > div > div > table > tbody",
        calorie="#feeding-guidelines-table > div > div > div > table > tbody > tr:last-child > td:nth-child(2)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Blackwood Pet Food")[0],
        ingredients="#main > div.product-tabs > div > div.tabs > div.tab.tab-ingredients > div.wp-block-group > div",
        analysis="#main > div.product-tabs > div > div.tabs > div.tab.tab-guaranteed-analysis > table > tbody",
        calorie="#main > div.product-tabs > div > div.tabs > div.tab.tab-guaranteed-analysis > table > tbody > tr:last-child > td"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Feline Natural")[0],
        ingredients="#accordion-container > div:nth-child(4) > div > p",
        analysis="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(1) > p:nth-child(2)",
        calorie="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(1) > p:nth-child(4)",
        additives="#accordion-container > div.accordion-content > div > table > tbody > tr > td:nth-child(2) > p:nth-child(2)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Leonardo Catfood")[0],
        ingredients="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(1) > p",
        analysis="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(2) > p",
        additives="#analyse-tab-pane > div > div > div.product-detail-analyse-text > div:nth-child(1) > div:nth-child(3) > p:nth-child(3)",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Lotus")[0],
        ingredients="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div:nth-child(1) > p",
        analysis="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div > div.row.mb-4 > div > div:nth-child(3)",
        calorie="#app > div > div.animated.fadeIn > div > div:nth-child(2) > div > div > div.tab-content > div.tab-pane > div > div > div > div > div:nth-child(3) > div > div:nth-child(3) > div:nth-child(4) > ul > li"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Nature's Logic")[0],
        ingredients="#av-layout-grid-1 > div.flex_cell.no_margin.av_one_half.el_after_av_cell_one_half.avia-builder-el-last.avia-full-stretch",
        analysis="#av-tab-section-1-2 > div > div > section > div > table",
        additives="#av-tab-section-1-4 > div > div > section > div > table",
        calorie="#av_section_2 > div > div > div > div > div.flex_column.av_one_fifth.el_after_av_one_fifth.avia-builder-el-last.flex_column_div.av-zero-column-padding > div > strong"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Terra Felis")[0],
        ingredients="#description-tab-pane > div > div.product-info-composition.tab-section > div > div > div > div.compostion-text-container.order-1.order-lg-2",
        analysis="#analytical-components-tab-pane > div > div > div > div > p > span",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="BlackHawk")[0],
        ingredients="#tabs-2 > div > p",
        analysis="#tabs-3 > div > table > tbody"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Catz finefood")[0],
        ingredients="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(3)",
        analysis="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(5)",
        calorie="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(4)",
        additives="body > div.page-wrap > section > div > div.content--wrapper > div > div.tab-menu--product.js--tab-menu > div.tab--container-list > div > div.tab--content > div.content--description > div.product--description > p:nth-child(6)",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="First Choice Canada")[0],
        ingredients="body > section.section.section--has-medium-padding.section--has-small-padding-bottom.section--has-smaller-padding-top-mobile > div > div > ul > li:nth-child(2) > div.accordion__item-content.js-accordion-item-content > p",
        analysis="body > section.section.section--has-medium-padding.section--has-small-padding-bottom.section--has-smaller-padding-top-mobile > div > div > ul > li:nth-child(3) > div.accordion__item-content.js-accordion-item-content > p",
        calorie="#tab-adult > table > tbody > tr:nth-child(10) > td > div.complex-table__footer-row.complex-table__footer-infos.grid.grid--justify-center.grid--align-center"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Monge")[0],
        ingredients="div.post-content > div.row.info_product > div > div.tab-content > div:nth-child(1) > p",
        analysis="div.post-content > div.row.info_product > div > div.tab-content > div:nth-child(2) > p",
        additives="div.post-content > div.row.info_product > div > div.tab-content > div:nth-child(3) > p"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Nature's Protection")[0],
        ingredients="#txt_cont > div.product_cont > div.data.aright > div.descr > div > table > tbody > tr > td.content.dazymas > div:nth-child(1) > div:nth-child(1) > div > span:nth-child(2)",
        analysis="#txt_cont > div.product_cont > div.data.aright > div.descr > div > table > tbody > tr > td.content.formos",
        additives="#txt_cont > div.product_cont > div.data.aright > div.descr > div > table > tbody > tr > td.content.dazymas > div:nth-child(1) > div:nth-child(4) > span:nth-child(3)",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Sheba")[0],
        ingredients="#content > article > div.product-details > div.tab.ingredients > div",
        analysis="#content > article > div.product-details > div.tab.nutrition > div",
        calorie="#content > article > div.product-details > div.tab.nutrition > div:nth-child(2)"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="SolidGold Petfood")[0],
        ingredients="#eael-advance-tabs-ca9134b > div.eael-tabs-content > div:nth-child(1) > span",
        analysis="#eael-advance-tabs-ca9134b > div.eael-tabs-content > div:nth-child(2) > table > tbody",
        calorie="#eael-advance-tabs-ca9134b > div.eael-tabs-content > div.clearfix > table > tbody > tr:last-child > td:last-child"
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Vigor and Sage")[0],
        ingredients="#tab-additional_information > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_composition > td > p:nth-child(1)",
        additives="#tab-additional_information > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_composition > td > p:nth-child(2)",
        analysis="#tab-additional_information > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_analytical-constituents > td > p",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="Vital Essentials")[0],
        ingredients="#chicken-freeze-dried-mini-patties-entree-2 > main > section.product-wrapper > div.tab-wrapper > div.tab.nutrition.clearfix > div:nth-child(1) > p",
        analysis="#chicken-freeze-dried-mini-patties-entree-2 > main > section.product-wrapper > div.tab-wrapper > div.tab.nutrition.clearfix > div:nth-child(2)",
    )[0]
    scraper.save()
    scraper = Crawler.objects.get_or_create(
        brand=Brand.objects.get_or_create(en_name="BOREAL")[0],
        ingredients="#content > div:nth-child(15) > h6:nth-child(2)",
        analysis="#content > div:nth-child(18) > p:nth-child(1)",
        calorie="#content > div:nth-child(18) > p:nth-child(3)"
    )
